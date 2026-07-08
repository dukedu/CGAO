"""
Xiaohongshu Crawler
"""

from cgao.core.browser import Browser
from cgao.pages.home_page import HomePage
from cgao.pages.search_page import SearchPage
from cgao.parsers.search_parser import SearchParser
from cgao.utils.scroll import ScrollManager


class XiaohongshuCrawler:

    def __init__(self, headless=None):

        self.browser = Browser(headless=headless)

        self.page = None

        self.home = None

    def open(self):

        self.browser.start()

        self.page = self.browser.new_page()

        self.home = HomePage(self.page)

    def close(self):

        self.browser.stop()

    def search(self, keyword: str):

        self.home.open()

        self.home.search(keyword)

    def collect(self, limit: int = 100):

        parser = SearchParser()

        page = SearchPage(self.page)

        scroll = ScrollManager(self.page)

        posts = {}

        empty_scroll = 0

        while len(posts) < limit:

            cards = page.cards()

            total = cards.count()

            if total == 0:

                break

            cards.last.scroll_into_view_if_needed()

            print(

                f"\rCollected: {len(posts)}/{limit} | Visible: {total}",

                end="",

                flush=True,

            )

            before = len(posts)

            for i in range(total):

                try:

                    post = parser.parse(

                        cards.nth(i)

                    )

                except Exception:

                    continue

                if post is None:

                    continue

                posts.setdefault(

                    post.note_id,

                    post

                )

                if len(posts) >= limit:

                    break

            if len(posts) == before:

                empty_scroll += 1

            else:

                empty_scroll = 0

            if empty_scroll >= 3:

                print("\nNo more new posts.")

                break

            if not scroll.scroll_until_new():

                print("\nReach end.")

                break

        print()

        return list(posts.values())