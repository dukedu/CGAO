import time


class ScrollManager:

    def __init__(self, page):

        self.page = page

    def page_height(self):

        return self.page.evaluate(
            "document.body.scrollHeight"
        )

    def scroll_once(self):

        self.page.mouse.wheel(0, 2500)

        time.sleep(2)

    def scroll_until_new(self):

        old = self.page_height()

        self.scroll_once()

        for _ in range(10):

            time.sleep(0.5)

            new = self.page_height()

            if new > old:

                return True

        return False