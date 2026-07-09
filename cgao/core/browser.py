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
    STATE_DIR,
    STATE_FILE,
    TIMEOUT,
    VIEWPORT,
)
from cgao.core.constants import USER_AGENT

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

        self.profile_dir = Path(

            STATE_DIR

        ) / "profile"

    # --------------------------------------------------

    def start(self):

        logger.info(

            "Launching Chromium..."

        )

        self.playwright = sync_playwright().start()

        kwargs = {

            "viewport": VIEWPORT,

            "user_agent": USER_AGENT,

            "locale": "zh-CN",

            "timezone_id": "Asia/Shanghai",

            "device_scale_factor": 1,

            "is_mobile": False,

            "has_touch": False,

        }

        self.profile_dir.mkdir(

            parents=True,

            exist_ok=True,

        )

        state = Path(

            STATE_FILE

        )

        if state.exists():

            logger.info(

                "Login state file found."

            )

        else:

            logger.warning(

                "No login state found."

            )

        logger.info(

            f"Using browser profile: {self.profile_dir}"

        )

        self.context = self.playwright.chromium.launch_persistent_context(

            user_data_dir=str(

                self.profile_dir

            ),

            headless=self.headless,

            **kwargs

        )

        if self.context.pages:

            self.page = self.context.pages[0]

        else:

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

        try:

            self.context.storage_state(

                path=str(

                    STATE_FILE

                ),

                indexed_db=True,

            )

        except TypeError:

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
