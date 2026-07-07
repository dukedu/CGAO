from cgao.crawler.xiaohongshu import XiaohongshuCrawler

crawler = XiaohongshuCrawler()

crawler.open()

crawler.goto_home()

print(crawler.navigator.title())

print(crawler.navigator.url())

input()

crawler.close()