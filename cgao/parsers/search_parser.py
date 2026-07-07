from urllib.parse import parse_qs, urlparse

from cgao.models.post import Post


class SearchParser:

    def _safe_text(self, locator):

        try:
            if locator.count() == 0:
                return ""

            return locator.first.inner_text(timeout=3000).strip()

        except Exception:
            return ""

    def _safe_attr(self, locator, attr):

        try:
            if locator.count() == 0:
                return None

            return locator.first.get_attribute(attr)

        except Exception:
            return None

    def _parse_like(self, text):

        if not text:
            return 0

        text = text.strip()

        try:

            if text.endswith("万"):
                return int(float(text[:-1]) * 10000)

            if text.endswith("亿"):
                return int(float(text[:-1]) * 100000000)

            return int(text.replace(",", ""))

        except Exception:

            return 0

    def parse(self, card):

        title = self._safe_text(
            card.locator("a.title span")
        )

        if not title:
            return None

        author = self._safe_text(
            card.locator(".name")
        )

        like_count = self._parse_like(
            self._safe_text(
                card.locator(".count")
            )
        )

        href = self._safe_attr(
            card.locator("a.cover"),
            "href"
        )

        if href is None:
            return None

        url = "https://www.xiaohongshu.com" + href

        note_id = href.split("?")[0].split("/")[-1]

        query = urlparse(href).query

        xsec_token = parse_qs(query).get(
            "xsec_token",
            [""]
        )[0]

        return Post(
            note_id=note_id,
            xsec_token=xsec_token,
            title=title,
            author=author,
            like_count=like_count,
            url=url
        )