import json
from pathlib import Path

from cgao.core import Browser
from cgao.core.config import STATE_FILE


LOGIN_URL = "https://www.xiaohongshu.com/explore"


def print_state_info(path: Path):

    if not path.exists():

        print()

        print("State file not found.")

        return

    data = json.loads(
        path.read_text(
            encoding="utf-8",
        )
    )

    cookies = data.get(
        "cookies",
        [],
    )

    origins = data.get(
        "origins",
        [],
    )

    domains = sorted(
        {
            cookie.get(
                "domain",
                "",
            )
            for cookie in cookies
            if (
                "xiaohongshu" in cookie.get("domain", "")
                or "rednote" in cookie.get("domain", "")
            )
        }
    )

    print()

    print("=" * 60)

    print(f"State file : {path}")

    print(f"Cookies    : {len(cookies)}")

    print(f"Origins    : {len(origins)}")

    print("Domains    :")

    for domain in domains:

        print(f"  - {domain}")

    print("=" * 60)


state_file = Path(STATE_FILE)

with Browser() as browser:

    page = browser.new_page()

    page.goto(
        LOGIN_URL,
        wait_until="domcontentloaded",
    )

    page.wait_for_timeout(3000)

    input(
        "\n请在浏览器里完成登录，确认页面右上角已是登录状态后按 Enter..."
    )

    page.wait_for_timeout(5000)

    browser.save_state()

    page.reload(
        wait_until="domcontentloaded",
    )

    page.wait_for_timeout(8000)

    input(
        "\n请确认刷新后仍然是登录状态，然后按 Enter 再保存一次..."
    )

    browser.save_state()

print_state_info(state_file)

print("\nDone.")
