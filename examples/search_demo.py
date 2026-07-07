from cgao.crawler.xiaohongshu import XiaohongshuCrawler

crawler = XiaohongshuCrawler(
    headless=False
)

try:

    crawler.open()

    crawler.search("DeepSeek")

    input("Press ENTER...")

finally:

    crawler.close()