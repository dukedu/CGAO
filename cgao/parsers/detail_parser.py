import re

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
                t.strip()
                for t in self.page.locator(selector).all_inner_texts()
            ]
        except:
            return []

    def _images(self):

        imgs = []

        try:

            loc = self.page.locator("img")

            for i in range(loc.count()):

                src = loc.nth(i).get_attribute("src")

                if not src:
                    continue

                if "sns-webpic" in src:

                    imgs.append(src)

        except:
            pass

        return list(dict.fromkeys(imgs))

    def _numbers(self):

        result = {

            "like": 0,

            "collect": 0,

            "comment": 0,

            "share": 0

        }

        try:

            text = self.page.locator("body").inner_text()

            nums = re.findall(r"\d+", text)

            if len(nums) >= 4:

                result["like"] = int(nums[0])

                result["collect"] = int(nums[1])

                result["comment"] = int(nums[2])

                result["share"] = int(nums[3])

        except:
            pass

        return result

    def parse(self, post: Post):

        post.content = self._text("#detail-desc")

        post.tags = self._texts("a[href*='/search_result']")

        post.images = self._images()

        text = self.page.locator("body").inner_text()

        m = re.search(

            r"\d{4}-\d{2}-\d{2}.*",

            text

        )

        if m:

            line = m.group()

            post.publish_time = line

            ip = re.search(

                r"IP.*?[:：]\s*(.*)",

                line

            )

            if ip:

                post.ip_location = ip.group(1)

        stat = self._numbers()

        post.like_count = stat["like"]

        post.collect_count = stat["collect"]

        post.comment_count = stat["comment"]

        post.share_count = stat["share"]

        return post