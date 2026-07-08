"""
CGAO Browser
"""

from __future__ import annotations

from pathlib import Path

from playwright.sync_api import BrowserContext
from playwright.sync_api import Page
from playwright.sync_api import Playwright
from playwright.sync_api import sync_playwright

from cgao.core.config import (
    HEADLESS,
    STATE_FILE,
    TIMEOUT,
    VIEWPORT,
)

from cgao.core.logger import logger


class Browser:

    def __init__(

        self,

        headless: bool | None = None,

    ):

        self.headless = (

            HEADLESS

            if headless is None

            else headless

        )

        self.playwright: Playwright | None = None

        self.browser = None

        self.context: BrowserContext | None = None

        self.page: Page | None = None

    # --------------------------------------------------

    def start(self):

        logger.info(

            "Launching Chromium..."

        )

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(

            headless=self.headless,

        )

        kwargs = {

            "viewport": VIEWPORT,

        }

        state = Path(

            STATE_FILE

        )

        if state.exists():

            logger.info(

                "Loading login state..."

            )

            kwargs["storage_state"] = str(

                state

            )

        else:

            logger.warning(

                "No login state found."

            )

        self.context = self.browser.new_context(

            **kwargs

        )

        self.page = self.context.new_page()

        self.page.set_default_timeout(

            TIMEOUT

        )

        logger.info(

            "Browser Ready."

        )

        return self

    # --------------------------------------------------

    def new_page(self):

        return self.page

    # --------------------------------------------------

    def save_state(self):

        if self.context is None:

            return

        Path(

            STATE_FILE

        ).parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        self.context.storage_state(

            path=str(

                STATE_FILE

            )

        )

        logger.info(

            "Login state saved."

        )

    # --------------------------------------------------

    def stop(self):

        if self.context:

            self.context.close()

            self.context = None

        if self.browser:

            self.browser.close()

            self.browser = None

        if self.playwright:

            self.playwright.stop()

            self.playwright = None

        logger.info(

            "Browser Closed."

        )

    # --------------------------------------------------

    def __enter__(self):

        return self.start()

    def __exit__(

        self,

        exc_type,

        exc,

        tb,

    ):

        self.stop()