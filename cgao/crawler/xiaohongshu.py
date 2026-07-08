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

        posts = {}

        db = SQLiteDatabase()

        existing = db.existing_ids()

        print(
            f"SQLite Existing : {len(existing)}"
        )

        new_posts = 0

        while len(posts) < limit:

            cards = search_page.cards()

            total = cards.count()

            print(
                f"\rCollected: {len(posts)}/{limit} | Visible: {total}",
                end="",
                flush=True,
            )

            for i in range(total):

                try:

                    card = cards.nth(i)

                    post = parser.parse(card)

                    if post is None:
                        continue

                    if post.note_id in existing:

                        continue

                    posts[post.note_id] = post

                    new_posts += 1

                    print(

                        f"\rExisting:{len(existing)} "

                        f"New:{new_posts} "

                        f"Total:{len(existing)+new_posts}",

                        end="",

                        flush=True

                    )

                except Exception:
                    continue

            if len(posts) >= limit:
                break

            if not scroll.scroll_until_new():

                print("\nNo more new posts.")

                break

        print()

        posts = list(posts.values())[:limit]

        db = SQLiteDatabase()

        for post in posts:

            db.insert(post)

        db.save()

        total = db.count()

        db.close()

        print()

        print("="*60)

        print(f"Existing : {len(existing)}")

        print(f"New      : {new_posts}")

        print(f"Total    : {total}")

        print("="*60)

        output_dir = Path("data/raw")

        output_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        csv_path = output_dir / f"{self.keyword}.csv"

        try:

            CSVExporter().export(

                posts,

                csv_path

            )

            print(f"CSV Saved -> {csv_path}")

        except Exception as e:

            print(e)

        print(f"CSV Saved -> {csv_path}")

        return posts