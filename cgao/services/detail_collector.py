from __future__ import annotations

from playwright.sync_api import Error
from playwright.sync_api import TimeoutError

from cgao.parsers import StateParser


class DetailCollector:

    def __init__(self, crawler):

        self.crawler = crawler

    def collect(self, post):

        page = self.crawler.page

        url = post.detail_url()

        self._goto(page, url)

        html = self._content(page)

        return StateParser.parse(html)

    def _goto(self, page, url: str):

        last_error = None

        for _ in range(3):

            try:

                page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=30000,
                )

                page.wait_for_timeout(2500)

                self._wait_idle(page)

                return

            except (TimeoutError, Error) as e:

                last_error = e

                page.wait_for_timeout(1500)

        if last_error:

            raise last_error

    def _wait_idle(self, page):

        try:

            page.wait_for_load_state(
                "networkidle",
                timeout=5000,
            )

        except TimeoutError:

            pass

    def _content(self, page) -> str:

        last_error = None

        for _ in range(5):

            try:

                page.wait_for_load_state(
                    "domcontentloaded",
                    timeout=5000,
                )

                return page.content()

            except (TimeoutError, Error) as e:

                last_error = e

                page.wait_for_timeout(1000)

        if last_error:

            raise last_error

        return ""
