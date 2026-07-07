"""
Cookie persistence utilities.
"""

import json
from pathlib import Path

COOKIE_DIR = Path("cgao/storage/cookie")
COOKIE_DIR.mkdir(parents=True, exist_ok=True)

COOKIE_FILE = COOKIE_DIR / "cookies.json"


class CookieManager:

    @staticmethod
    def save(context):

        cookies = context.cookies()

        with open(COOKIE_FILE, "w", encoding="utf-8") as f:
            json.dump(cookies, f, ensure_ascii=False, indent=2)

        print("Cookies saved.")

    @staticmethod
    def load(context):

        if COOKIE_FILE.exists():

            with open(COOKIE_FILE, "r", encoding="utf-8") as f:

                cookies = json.load(f)

            context.add_cookies(cookies)

            print("Cookies loaded.")