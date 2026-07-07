from cgao.crawler.browser import Browser
from cgao.crawler.cookie import CookieManager


class SessionManager:

    def __init__(self):

        self.browser = Browser()

        self.browser.start()

        self.context = self.browser.context

    def save_cookie(self):

        CookieManager.save(self.context)

    def load_cookie(self):

        CookieManager.load(self.context)

    def new_page(self):

        return self.browser.new_page()

    def close(self):

        self.browser.close()