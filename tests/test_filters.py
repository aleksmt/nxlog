from playwright.sync_api import expect

from pages.todo_page import TodoPage

todo_task_one_name = "Task 1"
todo_task_two_name = "Task 2"

def test_active_filter(todo_page: TodoPage):
    """Ensures only active items are shown in the 'Active' filter."""
    todo_page.add_todo(todo_task_one_name)
    todo_page.add_todo(todo_task_two_name)
    todo_page.mark_completed(1)

    todo_page.show_active()

    items = todo_page.get_items()

    expect(items).to_have_count(1)
    expect(items.nth(0)).to_have_text(todo_task_one_name)


def test_completed_filter(todo_page: TodoPage):
    """Ensures only completed items are shown in the 'Completed' filter."""
    todo_page.add_todo(todo_task_one_name)
    todo_page.mark_completed(0)

    todo_page.show_completed()

    items = todo_page.get_items()

    expect(items).to_have_count(1)
    expect(items.nth(0)).to_have_text(todo_task_one_name)
