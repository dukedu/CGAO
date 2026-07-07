from playwright.sync_api import Locator, Page


class SearchPage:

    def __init__(self, page: Page):

        self.page = page

    def cards(self) -> Locator:

        return self.page.locator("section.note-item")

    def count(self):

        return self.cards().count()