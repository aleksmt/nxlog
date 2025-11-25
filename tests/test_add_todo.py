import pytest
from playwright.sync_api import expect

from pages.todo_page import TodoPage


@pytest.mark.parametrize(
    "todo_task_name",
    [
        pytest.param("Go to gym", id="english"),
        pytest.param("Купить хлеб", id="i11n"),
        pytest.param("123 test", id="numbers"),
        pytest.param("❣️Marks & 🍩Donuts test", id="symbols"),
    ]
)
def test_add_todo(todo_page: TodoPage, todo_task_name: str):
    """
    Validates that a to-do item can be added with: English text, non-English text, numeric and emoji characters
    """
    todo_page.add_todo(todo_task_name)
    expect(todo_page.get_items()).to_contain_text(todo_task_name)
