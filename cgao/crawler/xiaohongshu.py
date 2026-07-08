"""
Xiaohongshu Crawler
"""

from pathlib import Path

from cgao.crawler.browser import Browser
from cgao.exporters.csv_exporter import CSVExporter
from cgao.pages.home_page import HomePage
from cgao.pages.search_page import SearchPage
from cgao.parsers.search_parser import SearchParser
from cgao.utils.scroll import ScrollManager
from cgao.database.sqlite import SQLiteDatabase


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

    def search(self, keyword: str):

        self.keyword = keyword

        self.home.open()

        self.home.search(keyword)

    def close(self):

        self.browser.stop()

    def collect(self, limit=100):

        search_page = SearchPage(self.page)

        parser = SearchParser()

        scroll = ScrollManager(self.page)

        db = SQLiteDatabase()

        existing = db.existing_ids()

        print(f"SQLite Existing : {len(existing)}")

        posts = {}

        empty_round = 0

        while len(posts) < limit:

            cards = search_page.cards()

            if cards.count() > 0:

                cards.last.scroll_into_view_if_needed()

            total = cards.count()

            print(
                f"\rExisting:{len(existing)} "
                f"New:{len(posts)} "
                f"Target:{limit} "
                f"Visible:{total}",
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

                    if post.note_id in existing:
                        continue

                    if post.note_id in posts:
                        continue

                    posts[post.note_id] = post

                except Exception:

                    continue

            after = len(posts)

            if after >= limit:

                break

            if after == before:

                empty_round += 1

            else:

                empty_round = 0

            if empty_round >= 3:

                print("\nReach end.")

                break

            if not scroll.scroll_until_new():

                break

        print()

        for post in posts.values():

            db.insert(post)

        db.save()

        total = db.count()

        db.close()

        posts = list(posts.values())

        output_dir = Path("data/raw")

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        csv_path = output_dir / f"{self.keyword}.csv"

        CSVExporter().export(
            posts,
            csv_path,
        )

        print()

        print("=" * 60)
        print(f"Existing : {len(existing)}")
        print(f"New      : {len(posts)}")
        print(f"Total    : {total}")
        print(f"CSV      : {csv_path}")
        print("=" * 60)

        return posts