"""
Home Page Object

Responsible for all interactions on Xiaohongshu home page.
"""

from playwright.sync_api import Page

from cgao.core.logger import logger


class HomePage:

    HOME_URL = "https://www.xiaohongshu.com/explore"

    def __init__(self, page: Page):

        self.page = page

    def open(self):

        logger.info("Opening Home Page...")

        self.page.goto(
            self.HOME_URL,
            wait_until="domcontentloaded"
        )

        self.page.wait_for_timeout(3000)

    def search(self, keyword: str):

        logger.info(f"Searching: {keyword}")

        # 这里先采用 Codegen 找到的 textbox
        search_box = self.page.get_by_role("textbox").first

        search_box.click()

        self.page.wait_for_timeout(300)

        # Mac
        search_box.press("Meta+A")

        self.page.wait_for_timeout(300)

        search_box.fill(keyword)

        self.page.wait_for_timeout(500)

        # 尝试 Enter
        search_box.press("Enter")

        self.page.wait_for_timeout(2000)

        logger.info("Search submitted.")