from cgao.core import Browser

with Browser() as browser:

    page = browser.new_page()

    page.goto(

        "https://www.xiaohongshu.com"

    )

    input(

        "\n登录完成后按 Enter 保存登录状态..."

    )

    browser.save_state()

print("\nDone.")