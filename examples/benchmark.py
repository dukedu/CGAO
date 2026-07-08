from cgao.crawler.xiaohongshu import XiaohongshuCrawler

KEYWORDS = [
    "DeepSeek",
    "ChatGPT",
    "Claude",
    "Gemini",
    "Midjourney",
]

LIMIT = 500

crawler = XiaohongshuCrawler(headless=False)

try:

    crawler.open()

    for keyword in KEYWORDS:

        print("\n" + "=" * 80)
        print(f"Keyword : {keyword}")
        print("=" * 80)

        crawler.search(keyword)

        posts = crawler.collect(limit=LIMIT)

        print(f"\nCollected : {len(posts)}")

finally:

    crawler.close()