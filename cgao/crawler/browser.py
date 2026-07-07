from pathlib import Path

from playwright.sync_api import Browser as PWBrowser
from playwright.sync_api import BrowserContext
from playwright.sync_api import Page
from playwright.sync_api import Playwright
from playwright.sync_api import sync_playwright

from cgao.config import HEADLESS, TIMEOUT, VIEWPORT
from cgao.logger import logger


STATE_FILE = Path("storage/state/xiaohongshu.json")


class Browser:

    def __init__(self, headless=HEADLESS):

        self.headless = headless

        self.playwright = None
        self.browser = None
        self.context = None

    def start(self):

        logger.info("Launching Chromium...")

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=self.headless
        )

        if STATE_FILE.exists():

            logger.info("Loading login state...")

            self.context = self.browser.new_context(
                viewport=VIEWPORT,
                storage_state=str(STATE_FILE)
            )

        else:

            logger.info("No login state found.")

            self.context = self.browser.new_context(
                viewport=VIEWPORT
            )

        logger.info("Browser Ready.")

    def new_page(self) -> Page:

        page = self.context.new_page()

        page.set_default_timeout(TIMEOUT)

        return page

    def save_state(self):

        STATE_FILE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self.context.storage_state(
            path=str(STATE_FILE)
        )

        logger.info("Login state saved.")

    def stop(self):

        if self.context:
            self.context.close()

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()

        logger.info("Browser Closed.")