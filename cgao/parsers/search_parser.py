from urllib.parse import urlparse, parse_qs

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

        text = text.replace(",", "").strip()

        try:

            if text.endswith("万"):

                return int(float(text[:-1]) * 10000)

            if text.endswith("亿"):

                return int(float(text[:-1]) * 100000000)

            return int(text)

        except Exception:

            return 0

    def _get_href(self, card):

        """
        Find the first search_result href.
        This is much more stable than relying on CSS classes.
        """

        links = card.locator("a[href]")

        count = links.count()

        for i in range(count):

            try:

                href = links.nth(i).get_attribute("href")

                if href and "/search_result/" in href:

                    return href

            except Exception:

                continue

        return None

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

        href = self._get_href(card)

        if href is None:

            return None

        if href.startswith("/"):

            href = "https://www.xiaohongshu.com" + href

        parsed = urlparse(href)

        note_id = parsed.path.split("/")[-1]

        query = parse_qs(parsed.query)

        xsec_token = query.get(

            "xsec_token",

            [""]

        )[0]

        xsec_source = query.get(

            "xsec_source",

            [""]

        )[0]

        return Post(

            note_id=note_id,

            title=title,

            author=author,

            like_count=like_count,

            url=href,

            xsec_token=xsec_token,

            xsec_source=xsec_source,

        )