import pytest
from _pytest.config import Config
from _pytest.config.argparsing import Parser
from playwright.sync_api import (
    Browser
)

@pytest.fixture(scope="session")
def app_host(pytestconfig: Config):
    """Returns the app_host value from the pytest configuration."""
    return pytestconfig.getini("app_host")

@pytest.fixture
def page(browser: Browser, app_host: str):
    """Creates a new Playwright Page Object and navigates to the full URL."""
    context = browser.new_context(base_url=app_host)
    page = context.new_page()
    yield page
    context.close()

def pytest_addoption(parser: Parser):
    parser.addini(
        name="app_host",
        help="Site host base for tests",
        default="https://demo.playwright.dev",
        type="string"
    )
