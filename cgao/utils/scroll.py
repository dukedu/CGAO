import time


class ScrollManager:

    def __init__(self, page):

        self.page = page

    def last_note(self):

        cards = self.page.locator("section.note-item")

        count = cards.count()

        if count == 0:

            return None

        try:

            href = cards.nth(count - 1).locator("a").first.get_attribute("href")

            return href

        except Exception:

            return None

    def scroll_until_new(self):

        last = self.last_note()

        self.page.mouse.wheel(0, 4000)

        for _ in range(20):

            time.sleep(0.3)

            current = self.last_note()

            if current != last:

                return True

        return False