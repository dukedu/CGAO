from __future__ import annotations

import re
import time

from bs4 import BeautifulSoup

from cgao.collector.base_collector import BaseCollector
from cgao.models import Post


class SearchCollector(BaseCollector):

    PATTERN = re.compile(
        r"/search_result/([0-9a-z]+)\?xsec_token=([^&]+)"
    )

    def collect(self, limit=100):

        posts = {}

        idle = 0

        while len(posts) < limit:

            html = self.page.content()

            soup = BeautifulSoup(
                html,
                "html.parser",
            )

            cards = soup.select(
                'a[href*="/search_result/"]'
            )

            before = len(posts)

            for card in cards:

                href = card.get(
                    "href",
                    "",
                )

                m = self.PATTERN.search(
                    href,
                )

                if not m:

                    continue

                note_id = m.group(1)

                xsec_token = m.group(2)

                title = ""

                author = ""

                spans = card.select("span")

                if spans:

                    title = spans[0].get_text(
                        strip=True,
                    )

                footer = (
                    card.find_parent()
                )

                if footer:

                    txt = footer.get_text(
                        " ",
                        strip=True,
                    )

                    txt = txt.replace(
                        title,
                        "",
                    ).strip()

                    author = txt.split(" ")[0]

                posts[note_id] = Post(
                    note_id=note_id,
                    xsec_token=xsec_token,
                    title=title,
                    author=author,
                )

            print(
                f"Collected : {len(posts)}"
            )

            if len(posts) >= limit:

                break

            if before == len(posts):

                idle += 1

            else:

                idle = 0

            if idle >= 3:

                break

            self.page.mouse.wheel(
                0,
                5000,
            )

            time.sleep(2)

        return list(posts.values())[:limit]