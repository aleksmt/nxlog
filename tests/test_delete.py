from playwright.sync_api import expect

from pages.todo_page import TodoPage

todo_task_name = "Remove me"

def test_delete(todo_page: TodoPage):
    """Ensures that deleting a to do removes it from the UI."""
    todo_page.add_todo(todo_task_name)
    expect(todo_page.get_items()).to_contain_text(todo_task_name)

    todo_page.delete_item(0)

    expect(todo_page.get_items()).to_have_count(0)
