from cgao.crawler.xiaohongshu import XiaohongshuCrawler

crawler = XiaohongshuCrawler(
    headless=False
)

crawler.open()

crawler.goto_home()

input("Press ENTER to quit...")

crawler.close()