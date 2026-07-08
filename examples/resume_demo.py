from cgao.crawler.xiaohongshu import XiaohongshuCrawler


crawler = XiaohongshuCrawler()

try:

    crawler.open()

    crawler.search("DeepSeek")

    crawler.collect(
        limit=1000
    )

finally:

    crawler.close()