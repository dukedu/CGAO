from pathlib import Path

from cgao.collector import SearchCollector
from cgao.core import Browser
from cgao.pages.home_page import HomePage


def main():

    browser = Browser()

    browser.start()

    page = browser.new_page()

    home = HomePage(page)

    home.open()

    home.search("DeepSeek")

    # 等搜索结果加载完成
    page.wait_for_timeout(5000)

    # 保存整个搜索页 HTML
    html = page.content()

    Path("search.html").write_text(
        html,
        encoding="utf-8",
    )

    print("✅ search.html 已保存")

    # 顺便测试 SearchCollector
    posts = SearchCollector(page).collect(limit=5)

    print(posts)

    browser.stop()


if __name__ == "__main__":
    main()