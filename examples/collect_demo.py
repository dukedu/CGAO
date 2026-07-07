from cgao.crawler.xiaohongshu import XiaohongshuCrawler

crawler = XiaohongshuCrawler(
    headless=False
)

try:

    crawler.open()

    crawler.search("DeepSeek")

    input("\n搜索完成后按 Enter 开始采集...")

    posts = crawler.collect(limit=5)

    print("\n")

    print("=" * 80)

    for i, post in enumerate(posts, start=1):

        print(f"[{i}]")

        print("Title :", post.title)

        print("Author:", post.author)

        print("Likes :", post.like_count)

        print("URL   :", post.url)

        print("-" * 80)

finally:

    crawler.close()