from cgao.collector import (
    DetailCollector,
    SearchCollector,
)
from cgao.core import Browser
from cgao.pages.home_page import HomePage


def main():

    browser = Browser()

    browser.start()

    page = browser.new_page()

    home = HomePage(page)

    home.open()

    home.search("DeepSeek")

    print()

    print("=" * 60)
    print("Collect Search")
    print("=" * 60)

    search = SearchCollector(page)

    posts = search.collect(limit=10)

    print(f"\nSearch : {len(posts)} posts\n")

    if not posts:

        print("No posts found.")

        browser.stop()

        return

    detail = DetailCollector(page)

    print("=" * 60)
    print("Collect Detail")
    print("=" * 60)

    results = detail.collect_many(posts)

    print()

    print("=" * 60)
    print(f"Success : {len(results)}")
    print("=" * 60)

    for item in results:

        p = item.post

        print()

        print("-" * 60)

        print(f"ID      : {p.note_id}")
        print(f"Title   : {p.title}")
        print(f"Author  : {p.author}")
        print(f"Like    : {p.like_count}")
        print(f"Comment : {p.comment_count}")
        print(f"Collect : {p.collect_count}")
        print(f"Share   : {p.share_count}")
        print(f"Images  : {len(item.images)}")
        print(f"Tags    : {len(item.tags)}")

    browser.stop()


if __name__ == "__main__":

    main()