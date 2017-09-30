from typing import Coroutine, Any, Union, Callable
from asyncio import AbstractEventLoop
from .user import User
from .game import Game
from .enums import Status


class Client:
    user: User
    loop: AbstractEventLoop

    async def on_error(self, event_method, *args, **kwargs) -> None: ...

    async def login(self, token: str, *, bot: bool = ...) -> None: ...

    async def logout(self) -> None: ...

    async def connect(self, *, reconnect: bool = ...) -> None: ...

    async def close(self) -> None: ...

    async def start(self, token: str, *, bot: bool = ..., reconnect: bool = ...) -> None: ...

    async def run(self, token: str, *, bot: bool = ..., reconnect: bool = ...) -> None: ...

    def is_closed(self) -> bool: ...

    def event(self, coro: Coroutine[Any, Any, Any]) -> Coroutine[Any, Any, Any]: ...

    def async_event(self,
                    coro: Union[
                        Callable[..., Any],
                        Coroutine[Any, Any, Any]
                    ]) -> Coroutine[Any, Any, Any]: ...

    async def change_presence(self, *, game: Game=None, status: Status=None, afk: bool=None) -> None: ...
