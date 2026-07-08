from cgao.crawler.xiaohongshu import XiaohongshuCrawler

crawler = XiaohongshuCrawler(
    headless=False
)

try:

    crawler.open()

    crawler.search("DeepSeek")

    print("\n开始自动采集...\n")

    posts = crawler.collect(limit=100)

    print()

    print("=" * 80)

    print(f"Collected {len(posts)} posts")

    print("=" * 80)

    for i, post in enumerate(posts[:10], start=1):

        print(f"[{i}]")

        print("Title :", post.title)

        print("Author:", post.author)

        print("Likes :", post.like_count)

        print("URL   :", post.url)

        print("-" * 80)

finally:

    crawler.close()