import pytest
from playwright.sync_api import Page

from pages.todo_page import TodoPage


@pytest.fixture
def todo_page(page: Page) -> TodoPage:
    """Initializes the TodoPage Page Object and navigates to the full URL."""
    todo_page = TodoPage(page)
    todo_page.goto()
    return todo_page
