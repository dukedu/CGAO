from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from playwright.sync_api import sync_playwright

from cgao.core import (
    HEADLESS,
    STATE_FILE,
    VIEWPORT,
)
from cgao.parsers import StateParser


class ThreadedDetailCollector:

    def __init__(

        self,

        workers: int = 5,

    ):

        self.workers = workers

    def _worker(self, post):

        with sync_playwright() as p:

            browser = p.chromium.launch(

                headless=HEADLESS,

            )

            context = browser.new_context(

                viewport=VIEWPORT,

                storage_state=str(STATE_FILE),

            )

            page = context.new_page()

            page.goto(

                post.detail_url(),

                wait_until="domcontentloaded",

            )

            page.wait_for_load_state(

                "networkidle"

            )

            html = page.content()

            result = StateParser.parse(

                html

            )

            browser.close()

            return result

    def collect(self, posts):

        results = []

        with ThreadPoolExecutor(

            max_workers=self.workers

        ) as executor:

            futures = [

                executor.submit(

                    self._worker,

                    post,

                )

                for post in posts

            ]

            for future in as_completed(

                futures

            ):

                try:

                    results.append(

                        future.result()

                    )

                except Exception as e:

                    print(e)

        return results