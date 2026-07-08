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

        self.keyword = None

    def open(self):

        self.browser.start()

        self.page = self.browser.new_page()

        self.home = HomePage(self.page)

    def close(self):

        self.browser.stop()

    def search(self, keyword: str):

        self.keyword = keyword

        self.home.open()

        self.home.search(keyword)

    def collect(self, limit=100):

        search_page = SearchPage(self.page)

        parser = SearchParser()

        scroll = ScrollManager(self.page)

        posts = {}

        empty_round = 0

        while len(posts) < limit:

            cards = search_page.cards()

            if cards.count() == 0:

                break

            cards.last.scroll_into_view_if_needed()

            total = cards.count()

            print(

                f"\rCollected:{len(posts)}/{limit} | Visible:{total}",

                end="",

                flush=True,

            )

            before = len(posts)

            for i in range(total):

                try:

                    card = cards.nth(i)

                    post = parser.parse(card)

                    if post is None:

                        continue

                    if post.note_id in posts:

                        continue

                    posts[post.note_id] = post

                    if len(posts) >= limit:

                        break

                except Exception:

                    continue

            if len(posts) >= limit:

                break

            if len(posts) == before:

                empty_round += 1

            else:

                empty_round = 0

            if empty_round >= 3:

                print("\nNo more new posts.")

                break

            if not scroll.scroll_until_new():

                print("\nScroll end.")

                break

        print()

        return list(posts.values())