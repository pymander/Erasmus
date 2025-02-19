from datetime import date, timedelta
from typing import Literal, overload
from typing_extensions import Self

from .datetime import DateTime
from .mixins.default import FormattableMixin
from .period import Period

class Date(FormattableMixin, date):
    def set(self, year: int = ..., month: int = ..., day: int = ...) -> Self: ...
    @property
    def day_of_week(self) -> int: ...
    @property
    def day_of_year(self) -> int: ...
    @property
    def week_of_year(self) -> int: ...
    @property
    def days_in_month(self) -> int: ...
    @property
    def week_of_month(self) -> int: ...
    @property
    def age(self) -> int: ...
    @property
    def quarter(self) -> int: ...
    def to_date_string(self) -> str: ...
    def to_formatted_date_string(self) -> str: ...
    def closest(self, dt1: date, dt2: date) -> Self: ...
    def farthest(self, dt1: date, dt2: date) -> Self: ...
    def is_future(self) -> bool: ...
    def is_past(self) -> bool: ...
    def is_leap_year(self) -> bool: ...
    def is_long_year(self) -> bool: ...
    def is_same_day(self, dt: date) -> bool: ...
    def is_anniversary(self, dt: date | None = ...) -> bool: ...
    def is_birthday(self, dt: date | None = ...) -> bool: ...
    def add(
        self, years: int = ..., months: int = ..., weeks: int = ..., days: int = ...
    ) -> Self: ...
    def subtract(
        self, years: int = ..., months: int = ..., weeks: int = ..., days: int = ...
    ) -> Self: ...
    def __add__(self, other: timedelta) -> Self: ...
    @overload
    def __sub__(self, other: timedelta) -> Self: ...
    @overload
    def __sub__(self, other: date) -> Period: ...
    def diff(self, dt: date = ..., abs: bool = ...) -> Period: ...
    def diff_for_humans(
        self, other: date | None = ..., absolute: bool = ..., locale: str = ...
    ) -> str: ...
    def start_of(
        self, unit: Literal['day', 'week', 'month', 'year', 'decade', 'century']
    ) -> Self: ...
    def end_of(
        self, unit: Literal['day', 'week', 'month', 'year', 'decade', 'century']
    ) -> Self: ...
    def next(self, day_of_week: int | None = ...) -> Self: ...
    def previous(self, day_of_week: int | None = ...) -> Self: ...
    def first_of(
        self, unit: Literal['month', 'quarter', 'year'], day_of_week: int | None = ...
    ) -> Self: ...
    def last_of(
        self, unit: Literal['month', 'quarter', 'year'], day_of_week: int | None = ...
    ) -> Self: ...
    def nth_of(
        self,
        unit: Literal['month', 'quarter', 'year'],
        nth: int,
        day_of_week: int | None,
    ) -> Self: ...
    def average(self, dt: date | None = ...) -> Self: ...
    @classmethod
    def today(cls) -> DateTime: ...
    @classmethod
    def fromtimestamp(cls, t: float) -> Self: ...
    @classmethod
    def fromordinal(cls, n: int) -> Self: ...
    def replace(
        self, year: int | None = ..., month: int | None = ..., day: int | None = ...
    ) -> Self: ...
