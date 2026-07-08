from __future__ import annotations

from cgao.parsers import StateParser


class DetailCollector:

    def __init__(self, crawler):

        self.crawler = crawler

    def collect(self, post):

        self.crawler.page.goto(
            post.detail_url(),
            wait_until="domcontentloaded",
        )

        self.crawler.page.wait_for_timeout(1500)

        html = self.crawler.page.content()

        return StateParser.parse(html)