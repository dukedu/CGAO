from cgao.crawler.xiaohongshu import XiaohongshuCrawler
from cgao.parsers.detail_parser import DetailParser

crawler = XiaohongshuCrawler()

try:

    crawler.open()

    crawler.search("DeepSeek")

    posts = crawler.collect(limit=1)

    if not posts:

        raise SystemExit("No posts.")

    post = posts[0]

    crawler.page.goto(
        post.detail_url(),
        wait_until="domcontentloaded"
    )

    crawler.page.wait_for_timeout(3000)

    parser = DetailParser(crawler.page)

    post = parser.parse(post)

    print()

    print("=" * 80)

    print("Title:")
    print(post.title)

    print()

    print("Content:")
    print(post.content)

    print()

    print("Tags:")
    print(post.tags)

    print()

    print("Images:")
    print(len(post.images))

    print("=" * 80)

finally:

    crawler.close()