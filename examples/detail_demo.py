from cgao.crawler.xiaohongshu import XiaohongshuCrawler
from cgao.parsers.state_parser import StateParser


crawler = XiaohongshuCrawler()

try:

    crawler.open()

    crawler.search("DeepSeek")

    posts = crawler.collect(limit=1)

    if not posts:
        raise RuntimeError("No posts found.")

    crawler.page.goto(
        posts[0].detail_url(),
        wait_until="domcontentloaded"
    )

    crawler.page.wait_for_timeout(3000)

    html = crawler.page.content()

    result = StateParser.parse(html)

    print()

    print("=" * 80)

    print(result.post)

    print()

    print(result.author)

    print()

    print(result.images)

    print()

    print(result.tags)

    print("=" * 80)

finally:

    crawler.close()