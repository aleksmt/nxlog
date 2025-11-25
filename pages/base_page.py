from abc import ABC

from playwright.sync_api import Page


class BasePage(ABC):
    """
    BasePage serves as an abstract base class for web pages, providing a framework
    to ensure that all subclasses define and use a `PATH` attribute for navigation.
    The class enforces type checking for the `page` argument passed into subclass
    constructors and facilitates navigation to the specified `PATH`.

    :ivar PATH: Represents the URL path for the page that subclasses must define.
    :type PATH: str
    """

    PATH: str = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        original_init = cls.__init__

        def wrapped_init(self, page: Page, *args, **kw):
            if not isinstance(page, Page):
                raise TypeError(f"{cls.__name__} expects first argument to be {type(Page)}")

            self.page = page

            original_init(self, page, *args, **kw)

        cls.__init__ = wrapped_init

    def goto(self) -> None:
        if not self.PATH:
            raise NotImplementedError(f"{self.__class__.__name__} must define PATH like '/path/to/page'")
        self.page.goto(self.PATH)
