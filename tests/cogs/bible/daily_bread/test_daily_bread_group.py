from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from attrs import define

from erasmus.cogs.bible.daily_bread.daily_bread_group import PassageFetcher
from erasmus.data import VerseRange
from erasmus.service_manager import ServiceManager

if TYPE_CHECKING:
    from unittest.mock import Mock

    from pytest_mock import MockerFixture

    from erasmus.types import Bible


@define(frozen=True)
class MockBible:
    id: int
    command: str
    name: str
    abbr: str
    service: str
    service_version: str
    rtl: bool | None = False
    books: int = 1
    book_mapping: dict[str, str] | None = None


class TestPassageFetcher:
    @pytest.fixture
    def mock_service_manager(self, mocker: MockerFixture) -> Mock:
        return mocker.create_autospec(ServiceManager)

    @pytest.fixture
    def bible1(self) -> Bible:
        return MockBible(
            id=1,
            command='bible1',
            name='Bible 1',
            abbr='BIB1',
            service='ServiceOne',
            service_version='service-BIB1',
        )

    @pytest.fixture
    def bible2(self) -> Bible:
        return MockBible(
            id=2,
            command='bible2',
            name='Bible 2',
            abbr='BIB2',
            service='ServiceTwo',
            service_version='service-BIB2',
        )

    def test_init(self, mock_service_manager: Mock) -> None:
        fetcher = PassageFetcher(
            VerseRange.from_string('Genesis 1:2'), mock_service_manager
        )

        assert fetcher.verse_range == VerseRange.from_string('Genesis 1:2')
        assert fetcher.service_manager is mock_service_manager
        assert fetcher.passage_map == {}

    async def test_call(
        self,
        mocker: MockerFixture,
        mock_service_manager: Mock,
        bible1: Bible,
        bible2: Bible,
    ) -> None:
        mock_service_manager.configure_mock(
            **{'get_passage.return_value': mocker.sentinel.get_passage_return}
        )
        fetcher = PassageFetcher(
            VerseRange.from_string('Genesis 1:2'), mock_service_manager
        )

        assert (await fetcher(bible2)) == mocker.sentinel.get_passage_return
        assert (await fetcher(bible1)) == mocker.sentinel.get_passage_return

        mock_service_manager.get_passage.assert_has_awaits(  # type: ignore
            [
                mocker.call(bible2, VerseRange.from_string('Genesis 1:2')),
                mocker.call(bible1, VerseRange.from_string('Genesis 1:2')),
            ]
        )

    async def test_call_cached(
        self,
        mocker: MockerFixture,
        mock_service_manager: Mock,
        bible1: Bible,
        bible2: Bible,
    ) -> None:
        mock_service_manager.configure_mock(
            **{'get_passage.return_value': mocker.sentinel.get_passage_return}
        )
        fetcher = PassageFetcher(
            VerseRange.from_string('Genesis 1:2'), mock_service_manager
        )

        await fetcher(bible2)
        await fetcher(bible1)

        mock_service_manager.get_passage.reset_mock()  # type: ignore

        assert (await fetcher(bible2)) == mocker.sentinel.get_passage_return
        assert (await fetcher(bible1)) == mocker.sentinel.get_passage_return

        mock_service_manager.get_passage.assert_not_awaited()  # type: ignore
