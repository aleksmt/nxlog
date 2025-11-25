from playwright.sync_api import expect

from pages.todo_page import TodoPage

todo_task_name = "Marks & Filters Completed"

def test_mark_completed(todo_page: TodoPage):
    """Verifies that completed items appear in the 'Completed' filter."""
    todo_page.add_todo(todo_task_name)
    todo_page.mark_completed(0)
    todo_page.show_completed()

    items = todo_page.get_items()

    expect(items).to_have_count(1)
    expect(items.nth(0)).to_have_text(todo_task_name)
