from __future__ import annotations

from cgao.collector.base_collector import BaseCollector


class CommentCollector(BaseCollector):

    def collect(self):

        comments = []

        items = self.page.locator(

            ".comment-item"

        )

        count = items.count()

        for i in range(count):

            item = items.nth(i)

            try:

                author = item.locator(

                    ".author"

                ).inner_text()

            except:

                author = ""

            try:

                content = item.locator(

                    ".content"

                ).inner_text()

            except:

                content = ""

            try:

                like = item.locator(

                    ".like"

                ).inner_text()

            except:

                like = "0"

            comments.append(

                {

                    "author": author,

                    "content": content,

                    "like": like,

                }

            )

        return comments