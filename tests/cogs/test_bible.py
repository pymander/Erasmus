from __future__ import annotations

from typing import TYPE_CHECKING, Any

import pytest

from erasmus.cogs.bible import Bible, BibleAppCommands

if TYPE_CHECKING:
    from unittest.mock import Mock

    from pytest_mock import MockerFixture

    from erasmus.erasmus import Erasmus
    from erasmus.service_manager import ServiceManager


class MockBot:
    config: Any = {}
    session: Any = {}


class MockServiceManager:
    ...


@pytest.fixture
def mock_bot(mocker: MockerFixture) -> Mock:
    bot = mocker.Mock()
    bot.config = mocker.Mock()
    bot.session = mocker.Mock()

    return bot


class TestBible:
    @pytest.fixture
    def mock_service_manager(self) -> MockServiceManager:
        return MockServiceManager()

    def test_instantiate(
        self, mock_bot: Erasmus, mock_service_manager: ServiceManager
    ) -> None:
        cog = Bible(mock_bot, mock_service_manager)
        assert cog is not None


class TestBibleAppCommands:
    @pytest.fixture
    def mock_service_manager(self) -> MockServiceManager:
        return MockServiceManager()

    def test_instantiate(
        self, mock_bot: Erasmus, mock_service_manager: ServiceManager
    ) -> None:
        cog = BibleAppCommands(mock_bot, mock_service_manager)
        assert cog is not None
