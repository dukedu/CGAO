from __future__ import annotations

from playwright.sync_api import TimeoutError

from cgao.collector.base_collector import BaseCollector
from cgao.parsers.state_parser import StateParser


class DetailCollector(BaseCollector):

    def collect(self, post):

        url = post.detail_url()

        print(f"Open Detail : {url}")

        self.page.goto(
            url,
            wait_until="domcontentloaded",
        )

        try:
            self.page.wait_for_load_state(
                "networkidle",
                timeout=5000,
            )
        except TimeoutError:
            pass

        html = self.page.content()

        result = StateParser.parse(html)

        return result

    def collect_many(self, posts):

        results = []

        total = len(posts)

        for index, post in enumerate(posts, start=1):

            print(
                f"[{index}/{total}] {post.note_id}"
            )

            try:

                result = self.collect(post)

                results.append(result)

            except Exception as e:

                print(e)

                continue

        return results