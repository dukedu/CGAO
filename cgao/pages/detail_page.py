from playwright.sync_api import Page


class DetailPage:

    def __init__(self, page: Page):

        self.page = page

    def open(self, url: str):

        self.page.goto(
            url,
            wait_until="domcontentloaded"
        )

        self.page.wait_for_timeout(3000)

    def title(self):

        return self.page.title()