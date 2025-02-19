import contextlib
from collections.abc import Iterator, Mapping
from typing import Any, ClassVar
from typing_extensions import Self

import attr

from ..syntax import ast as _FTL

MAX_PART_LENGTH: int = ...

@attr.s
class CurrentEnvironment:
    args: Any = ...
    error_for_missing_arg: bool = ...

@attr.s
class ResolverEnvironment:
    context: Any = ...
    errors: Any = ...
    part_count: Any = ...
    active_patterns: Any = ...
    current: Any = ...
    @contextlib.contextmanager
    def modified(self, **replacements: Any) -> Iterator[Self]: ...
    def modified_for_term_reference(
        self, args: Mapping[str, Any] | None = ...
    ) -> contextlib._GeneratorContextManager[Self]: ...

class BaseResolver:
    def __call__(self, env: ResolverEnvironment) -> Any: ...

class Literal(BaseResolver): ...
class EntryResolver(BaseResolver): ...

class Message(_FTL.Message, EntryResolver):
    value: Pattern | TextElement | None
    attributes: dict[str, TextElement]
    def __init__(self, id: str, **kwargs: Any) -> None: ...

class Term(_FTL.Term, EntryResolver):
    value: Pattern | TextElement | None
    attributes: dict[str, TextElement]
    def __init__(self, id: str, value: Any, **kwargs: Any) -> None: ...

class Pattern(_FTL.Pattern, BaseResolver):
    MAX_PARTS: ClassVar[int] = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, env: ResolverEnvironment) -> str: ...

def resolve(fluentish: Any, env: Any) -> Any: ...

class TextElement(_FTL.TextElement, Literal):
    def __call__(self, env: ResolverEnvironment) -> str: ...

class Placeable(_FTL.Placeable, BaseResolver):
    def __call__(self, env: ResolverEnvironment) -> str: ...

class NeverIsolatingPlaceable(_FTL.Placeable, BaseResolver):
    def __call__(self, env: ResolverEnvironment) -> str: ...

class StringLiteral(_FTL.StringLiteral, Literal):
    def __call__(self, env: ResolverEnvironment) -> str: ...

class NumberLiteral(_FTL.NumberLiteral, BaseResolver):
    def __init__(self, value: Any, **kwargs: Any) -> None: ...
    def __call__(self, env: ResolverEnvironment) -> str: ...

class EntryReference(BaseResolver):
    def __call__(self, env: ResolverEnvironment) -> str: ...

class MessageReference(_FTL.MessageReference, EntryReference): ...

class TermReference(_FTL.TermReference, EntryReference):
    def __call__(self, env: ResolverEnvironment) -> str: ...

class VariableReference(_FTL.VariableReference, BaseResolver):
    def __call__(self, env: ResolverEnvironment) -> str: ...

class Attribute(_FTL.Attribute, BaseResolver): ...

class SelectExpression(_FTL.SelectExpression, BaseResolver):
    def __call__(self, env: ResolverEnvironment) -> str: ...
    def select_from_select_expression(self, env: Any, key: Any) -> Any: ...

def is_number(val: Any) -> bool: ...
def match(val1: Any, val2: Any, env: Any) -> bool: ...

class Variant(_FTL.Variant, BaseResolver): ...

class Identifier(_FTL.Identifier, BaseResolver):
    def __call__(self, env: ResolverEnvironment) -> str: ...

class CallArguments(_FTL.CallArguments, BaseResolver): ...

class FunctionReference(_FTL.FunctionReference, BaseResolver):
    def __call__(self, env: ResolverEnvironment) -> str: ...

class NamedArgument(_FTL.NamedArgument, BaseResolver): ...
