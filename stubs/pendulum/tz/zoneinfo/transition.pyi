from datetime import timedelta

from .transition_type import TransitionType

class Transition:
    def __init__(
        self, at: int, ttype: TransitionType, previous: Transition | None
    ) -> None: ...
    @property
    def at(self) -> int: ...
    @property
    def local(self) -> int: ...
    @property
    def to(self) -> int: ...
    @property
    def to_utc(self) -> int: ...
    @property
    def ttype(self) -> TransitionType: ...
    @property
    def previous(self) -> Transition | None: ...
    @property
    def fix(self) -> int: ...
    def is_ambiguous(self, stamp: int) -> bool: ...
    def is_missing(self, stamp: int) -> bool: ...
    def utcoffset(self) -> timedelta: ...
    def __contains__(self, stamp: int) -> bool: ...
