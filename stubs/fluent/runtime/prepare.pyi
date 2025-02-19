from typing import Any

class Compiler:
    def __call__(self, item: Any) -> Any: ...
    def compile(self, node: Any) -> Any: ...
    def compile_generic(self, nodename: Any, **kwargs: Any) -> Any: ...
    def compile_Placeable(self, _: Any, expression: Any, **kwargs: Any) -> Any: ...
    def compile_Pattern(self, _: Any, elements: Any, **kwargs: Any) -> Any: ...
