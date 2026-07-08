"""
Crawler Service
"""

from cgao.crawler.xiaohongshu import XiaohongshuCrawler


class CrawlerService:

    def __init__(self, headless=False):
        self.headless = headless

    def search_and_collect(self, keyword: str, limit: int = 10):

        crawler = XiaohongshuCrawler(headless=self.headless)

        try:

            crawler.open()

            crawler.search(keyword)

            input("\nSearch finished. Press ENTER to collect...")

            posts = crawler.collect(limit)

            return posts

        finally:

            crawler.close()