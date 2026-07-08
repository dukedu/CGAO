from cgao.models.post import Post


class DetailParser:

    def __init__(self, page):

        self.page = page

    def _text(self, selector):

        try:

            return self.page.locator(selector).first.inner_text().strip()
        except:
            return ""

    def _texts(self, selector):

        try:
            return [
                x.strip()
                for x in self.page.locator(selector).all_inner_texts()
            ]
        except:
            return []

    def _images(self):

        images = []

        try:

            loc = self.page.locator("img")

            for i in range(loc.count()):

                src = loc.nth(i).get_attribute("src")

                if not src:
                    continue

                if "sns-webpic" not in src:
                    continue

                images.append(src)

        except:
            pass

        return list(dict.fromkeys(images))

    def parse(self, post: Post):

        post.content = self._text("#detail-desc")

        post.tags = self._texts(
            "a[href*='/search_result']"
        )

        post.images = self._images()

        return post