from typing import List

from playwright.async_api import Page, Locator

from pages.base_page import BasePage


class TodoPage(BasePage):
    """
    Page Object for the TodoMVC demo application
    Exposes locators for UI elements and high-level interactions such as adding, completing, filtering, deleting todos
    """

    PATH = "/todomvc/#/"

    def __init__(self, page: Page):
        """
        Initializes all locators for the TodoMVC page
        :param page: Playwright Page object
        """
        self.page: Page = page

        self.new_todo: Locator = page.locator("input.new-todo")
        self.todo_items: Locator = page.locator(".todo-list li")
        self.filter_all: Locator = page.locator("[href='#/']")
        self.filter_active: Locator = page.locator("[href='#/active']")
        self.filter_completed: Locator = page.locator("[href='#/completed']")

    def add_todo(self, text: str) -> None:
        """Adds a new to-do item by typing text and pressing enter"""
        self.new_todo.fill(text)
        self.new_todo.press("Enter")

    def get_items(self) -> Locator:
        """Returns the Locator collection of all todo list items"""
        return self.todo_items

    def get_items_text(self) -> list[str]:
        """Returns text from each to-do list item"""
        return self.todo_items.all_inner_texts()

    def mark_completed(self, index: int) -> None:
        """Marks the to-do at the given index as completed"""
        self.todo_items.nth(index).locator(".toggle").check()

    def delete_item(self, index: int) -> None:
        """Deletes a to-do at the given index. The delete button only appears on hover"""
        item = self.todo_items.nth(index)
        item.hover()
        item.locator(".destroy").click()

    def show_active(self) -> None:
        """Applies the 'Active' filter"""
        self.filter_active.click()

    def show_completed(self) -> None:
        """Applies the 'Completed' filter"""
        self.filter_completed.click()

    def show_all(self) -> None:
        """Resets the filter to show all items"""
        self.filter_all.click()
