"""
Navigator

Responsible for all page navigation.
"""

from playwright.sync_api import Page


class Navigator:

    def __init__(self, page: Page):

        self.page = page

    def open(self, url: str):

        self.page.goto(url)

        self.page.wait_for_load_state("networkidle")

    def title(self):

        return self.page.title()

    def url(self):

        return self.page.url