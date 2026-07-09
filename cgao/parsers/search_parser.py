from __future__ import annotations

import re
from urllib.parse import parse_qs
from urllib.parse import urlparse

from playwright.sync_api import Locator

from cgao.models import Post


class SearchParser:

    def parse(self, card: Locator):

        href = self._find_href(card)

        if not href:

            return None

        note_id = self._note_id(href)

        if not note_id:

            return None

        return Post(
            note_id=note_id,
            xsec_token=self._xsec_token(href),
        )

    def _find_href(self, card: Locator) -> str:

        links = card.locator("a").all()

        fallback = ""

        for link in links:

            try:

                href = link.get_attribute("href") or ""

            except Exception:

                continue

            if not href:

                continue

            if (
                "/explore/" in href
                or "/search_result/" in href
            ):

                return href

            fallback = href

        return fallback

    def _note_id(self, href: str) -> str:

        patterns = (
            r"/explore/([A-Za-z0-9]+)",
            r"/search_result/([A-Za-z0-9]+)",
        )

        for pattern in patterns:

            match = re.search(
                pattern,
                href,
            )

            if match:

                return match.group(1)

        return ""

    def _xsec_token(self, href: str) -> str:

        query = urlparse(href).query

        params = parse_qs(query)

        values = params.get("xsec_token") or []

        if not values:

            return ""

        return values[0]
