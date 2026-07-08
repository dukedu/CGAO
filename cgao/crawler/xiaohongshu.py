"""
Xiaohongshu Crawler
"""

from cgao.crawler.browser import Browser
from cgao.pages.home_page import HomePage
from cgao.pages.search_page import SearchPage
from cgao.parsers.search_parser import SearchParser
from cgao.utils.scroll import ScrollManager


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

    def collect(self, limit=100):

        search_page = SearchPage(self.page)

        parser = SearchParser()

        scroll = ScrollManager(self.page)

        posts = {}

        while len(posts) < limit:

            cards = search_page.cards()

            total = cards.count()

            print(f"\rCollected: {len(posts)} | Visible: {total}", end="")

            for i in range(total):

                try:

                    card = cards.nth(i)

                    post = parser.parse(card)

                    if post is None:
                        continue

                    posts[post.note_id] = post

                except Exception:
                    continue

            if len(posts) >= limit:
                break

            if not scroll.scroll_until_new():
                break

        print()

        return list(posts.values())[:limit]