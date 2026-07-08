import argparse

from cgao.crawler.xiaohongshu import XiaohongshuCrawler


parser = argparse.ArgumentParser()

parser.add_argument(
    "--keyword",
    default="DeepSeek"
)

parser.add_argument(
    "--limit",
    type=int,
    default=100
)

args = parser.parse_args()


crawler = XiaohongshuCrawler(
    headless=False
)

try:

    crawler.open()

    crawler.search(args.keyword)

    posts = crawler.collect(
        limit=args.limit
    )

    print()

    print("=" * 80)

    print(f"Collected {len(posts)} posts")

    print("=" * 80)

finally:

    crawler.close()