from collections.abc import Iterator
from datetime import date, timedelta
from typing import overload
from typing_extensions import Self

from .duration import Duration

class Period(Duration):
    def __new__(cls, start: date, end: date, absolute: bool = ...) -> Self: ...
    def __init__(self, start: date, end: date, absolute: bool = ...) -> None: ...
    @property
    def years(self) -> int: ...
    @property
    def months(self) -> int: ...
    @property
    def weeks(self) -> int: ...
    @property
    def days(self) -> int: ...
    @property
    def remaining_days(self) -> int: ...
    @property
    def hours(self) -> int: ...
    @property
    def minutes(self) -> int: ...
    @property
    def start(self) -> date: ...
    @property
    def end(self) -> date: ...
    def in_years(self) -> int: ...
    def in_months(self) -> int: ...
    def in_weeks(self) -> int: ...
    def in_days(self) -> int: ...
    def in_words(self, locale: str | None = ..., separator: str = ...) -> str: ...
    def range(self, unit: str, amount: int = ...) -> Iterator[date]: ...
    def as_interval(self) -> Duration: ...
    def __iter__(self) -> Iterator[date]: ...
    def __contains__(self, item: date) -> bool: ...
    def __add__(self, other: timedelta) -> Duration: ...
    def __radd__(self, other: timedelta) -> Duration: ...
    def __sub__(self, other: timedelta) -> Duration: ...
    def __neg__(self) -> Self: ...
    def __mul__(self, other: float) -> Duration: ...
    def __rmul__(self, other: float) -> Duration: ...
    @overload
    def __floordiv__(self, other: timedelta) -> int: ...
    @overload
    def __floordiv__(self, other: int) -> Duration: ...
    @overload
    def __truediv__(self, other: timedelta) -> float: ...
    @overload
    def __truediv__(self, other: float) -> Duration: ...
    @overload
    def __div__(self, other: timedelta) -> int: ...
    @overload
    def __div__(self, other: int) -> Duration: ...
    def __mod__(self, other: timedelta) -> Duration: ...
    def __divmod__(self, other: timedelta) -> tuple[int, Duration]: ...
    def __abs__(self) -> Self: ...
    def __reduce__(self) -> tuple[type[Self], tuple[date, date, bool]]: ...
    def __reduce_ex__(
        self, protocol: int
    ) -> tuple[type[Self], tuple[date, date, bool]]: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
