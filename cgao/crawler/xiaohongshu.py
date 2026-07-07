"""
Xiaohongshu Crawler
"""

from cgao.crawler.browser import Browser
from cgao.pages.home_page import HomePage
from cgao.pages.search_page import SearchPage
from cgao.parsers.search_parser import SearchParser


class XiaohongshuCrawler:

    def __init__(self, headless=False):

        self.browser = Browser(headless=headless)

        self.page = None

        self.home = None

    def open(self):

        self.browser.start()

        self.page = self.browser.new_page()

        self.home = HomePage(self.page)

    def search(self, keyword: str):

        self.home.open()

        self.home.search(keyword)

    def close(self):

        self.browser.stop()

    def collect(self, limit=10):

        search_page = SearchPage(self.page)

        parser = SearchParser()

        cards = search_page.cards()

        total = min(cards.count(), limit)

        print(f"\nFound {total} posts\n")

        posts = []

        for i in range(total):

            try:

                card = cards.nth(i)

                post = parser.parse(card)

                if post is None:

                    print(f"Skip Card {i}")

                    continue

                posts.append(post)

            except Exception as e:

                print(f"Card {i} Failed")

                print(e)

                continue

        return posts