from __future__ import annotations

from playwright.sync_api import Locator

from cgao.models import Post


class SearchParser:

    @staticmethod
    def _text(node, selector):

        try:

            return node.locator(

                selector

            ).inner_text().strip()

        except Exception:

            return ""

    @staticmethod
    def _attr(node, selector, name):

        try:

            return node.locator(

                selector

            ).get_attribute(

                name

            ) or ""

        except Exception:

            return ""

    def parse(

        self,

        card: Locator,

    ):

        href = self._attr(

            card,

            "a",

            "href",

        )

        if "/explore/" not in href:

            return None

        note_id = href.split(

            "/explore/"

        )[-1].split("?")[0]

        post = Post(

            note_id=note_id,

            title=self._text(

                card,

                ".title",

            ),

            author=self._text(

                card,

                ".author",

            ),

        )

        return post