# Service for querying biblegateway.com
from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import List

from attr import attrib, dataclass
from botus_receptus import re
from bs4 import BeautifulSoup, NavigableString, SoupStrainer, Tag
from yarl import URL

from ..data import Passage, SearchResults, VerseRange
from ..exceptions import DoNotUnderstandError
from ..protocols import Bible
from .base_service import BaseService

total_re = re.compile(re.START, re.named_group('total')(re.one_or_more(re.DIGITS)))


# TODO: Error handling
@dataclass(slots=True)
class BibleGateway(BaseService):
    _passage_url: URL = attrib(init=False)
    _search_url: URL = attrib(init=False)

    def __attrs_post_init__(self) -> None:
        self._passage_url = URL('https://www.biblegateway.com/passage/')
        self._search_url = URL('https://www.biblegateway.com/quicksearch/')

    def _transform_verse_node(
        self,
        bible: Bible,
        verses: VerseRange,
        verse_node: Tag,
        for_search: bool = False,
    ) -> Passage:
        for node in verse_node.select(
            f'h1, {"h3, " if not for_search else ""}.footnotes, .footnote, .crossrefs, '
            '.crossreference, .full-chap-link'
        ):
            # Remove headings and footnotes
            node.decompose()

        for number in verse_node.select('span.chapternum'):
            number.insert_before('__BOLD__')
            number.insert_after('__BOLD__ ')
            number.string = '1.'
            number.unwrap()
        for small_caps in verse_node.select('.small-caps'):
            for descendant in list(small_caps.descendants):
                if isinstance(descendant, NavigableString):
                    descendant.replace_with(descendant.string.upper())
            small_caps.unwrap()
        for bold in verse_node.select('b, h4'):
            bold.insert_before('__BOLD__')
            bold.insert_after('__BOLD__' + (' ' if bold.name == 'h4' else ''))
            bold.unwrap()
        for number in verse_node.select('sup.versenum'):
            # Add a period after verse numbers
            number.insert_before('__BOLD__')
            number.insert_after('__BOLD__ ')
            number.string = f'{number.string.strip()}.'
            number.unwrap()
        for br in verse_node.select('br'):
            br.replace_with('\n')
        for italic in verse_node.select('.selah, i, h3'):
            italic.insert_before('__ITALIC__')
            italic.insert_after('__ITALIC__')
            italic.unwrap()

        text = self._replace_special_escapes(bible, verse_node.get_text(''))

        return Passage(text=text, range=verses, version=bible.abbr)

    @asynccontextmanager
    async def _request_passage(
        self, bible: Bible, verses: VerseRange
    ) -> AsyncIterator[Passage]:
        async with self.get(
            self._passage_url.with_query(
                {
                    'search': str(verses),
                    'version': bible.service_version,
                    'interface': 'print',
                }
            )
        ) as response:
            text = await response.text(errors='replace')
            strainer = SoupStrainer(
                class_=re.compile(
                    re.WORD_BOUNDARY,
                    'result-text-style-',
                    re.either('normal', 'rtl'),
                    re.WORD_BOUNDARY,
                )
            )
            soup = BeautifulSoup(text, 'html.parser', parse_only=strainer)
            verse_block = soup.select_one(
                '.result-text-style-normal, .result-text-style-rtl'
            )

            if verse_block is None:
                raise DoNotUnderstandError

            yield self._transform_verse_node(bible, verses, verse_block)

    @asynccontextmanager
    async def _request_search(
        self, bible: Bible, terms: List[str], *, limit: int, offset: int
    ) -> AsyncIterator[SearchResults]:
        async with self.get(
            self._search_url.with_query(
                {
                    'quicksearch': ' '.join(terms),
                    'version': bible.service_version,
                    'limit': limit,
                    'interface': 'print',
                    'startnumber': offset + 1,
                }
            )
        ) as response:
            text = await response.text(errors='replace')
            strainer = SoupStrainer(class_=['search-result-list', 'showing-results'])
            soup = BeautifulSoup(text, 'html.parser', parse_only=strainer)

            verse_nodes = soup.select('.search-result-list .bible-item')
            total_node = soup.select_one('.showing-results')

            if verse_nodes is None or total_node is None:
                yield SearchResults([], 0)
                return

            if (match := total_re.match(total_node.get_text(' ', strip=True))) is None:
                raise DoNotUnderstandError

            def mapper(node: Tag) -> Passage:
                extras_node = node.select_one('.bible-item-extras')
                if extras_node:
                    extras_node.decompose()

                verse_text_node = node.select_one('.bible-item-text')
                verse_reference_node = node.select_one('.bible-item-title')

                if verse_text_node is None or verse_reference_node is None:
                    raise DoNotUnderstandError

                verse = VerseRange.from_string(verse_reference_node.string.strip())

                return self._transform_verse_node(bible, verse, verse_text_node, True)

            passages = list(map(mapper, verse_nodes))

            yield SearchResults(passages, int(match.group('total')))
