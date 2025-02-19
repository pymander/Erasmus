from collections.abc import Callable
from typing import Literal
from typing_extensions import Final

class ParserStream:
    string: str
    index: int
    peek_offset: int
    def __init__(self, string: str) -> None: ...
    def get(self, offset: int) -> str | None: ...
    def char_at(self, offset: int) -> str | None: ...
    @property
    def current_char(self) -> str | None: ...
    @property
    def current_peek(self) -> str | None: ...
    def next(self) -> str | None: ...
    def peek(self) -> str | None: ...
    def reset_peek(self, offset: int = ...) -> None: ...
    def skip_to_peek(self) -> None: ...

EOL: Final[str] = ...
EOF: Final[str] = ...
SPECIAL_LINE_START_CHARS: Final[tuple[str, ...]] = ...

class FluentParserStream(ParserStream):
    def peek_blank_inline(self) -> str: ...
    def skip_blank_inline(self) -> str: ...
    def peek_blank_block(self) -> str: ...
    def skip_blank_block(self) -> str: ...
    def peek_blank(self) -> None: ...
    def skip_blank(self) -> None: ...
    def expect_char(self, ch: str) -> Literal[True]: ...
    def expect_line_end(self) -> Literal[True]: ...
    def take_char(self, f: Callable[[str], bool]) -> str | Literal[False]: ...
    def is_char_id_start(self, ch: str) -> bool: ...
    def is_identifier_start(self) -> bool: ...
    def is_number_start(self) -> bool: ...
    def is_char_pattern_continuation(self, ch: str) -> bool: ...
    def is_value_start(self) -> bool: ...
    def is_value_continuation(self) -> bool: ...
    def is_next_line_comment(self, level: int = ...) -> bool: ...
    def is_variant_start(self) -> bool: ...
    def is_attribute_start(self) -> bool: ...
    def skip_to_next_entry_start(self, junk_start: int) -> None: ...
    def take_id_start(self) -> str: ...
    def take_id_char(self) -> str | Literal[False]: ...
    def take_digit(self) -> str | Literal[False]: ...
    def take_hex_digit(self) -> str | Literal[False]: ...
