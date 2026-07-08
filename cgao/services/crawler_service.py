from __future__ import annotations

from cgao.crawler.xiaohongshu import XiaohongshuCrawler


class CrawlerService:

    def __init__(self, headless=None):

        self.crawler = XiaohongshuCrawler(
            headless=headless
        )

    def open(self):

        self.crawler.open()

    def close(self):

        self.crawler.close()

    def search(
        self,
        keyword: str,
    ):

        self.crawler.search(keyword)

    def collect(
        self,
        keyword: str,
        limit: int = 100,
    ):

        self.open()

        self.search(keyword)

        return self.crawler.collect(limit)