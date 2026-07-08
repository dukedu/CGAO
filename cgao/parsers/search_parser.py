from __future__ import annotations

import re

from playwright.sync_api import Locator

from cgao.models import Post


class SearchParser:

    def parse(self, card: Locator):

        href = ""

        links = card.locator("a").all()

        for a in links:

            try:
                href = a.get_attribute("href") or ""
            except Exception:
                continue

            if "/explore/" in href:
                break

        if "/explore/" not in href:
            return None

        m = re.search(r"/explore/([A-Za-z0-9]+)", href)

        if not m:
            return None

        return Post(
            note_id=m.group(1)
        )