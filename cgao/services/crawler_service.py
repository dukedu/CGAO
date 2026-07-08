from cgao.crawler.xiaohongshu import XiaohongshuCrawler


class CrawlerService:

    def __init__(self):

        self.crawler = XiaohongshuCrawler()

    def collect(

        self,

        keyword,

        limit=100,

    ):

        self.crawler.open()

        self.crawler.search(keyword)

        posts = self.crawler.collect(limit)

        self.crawler.close()

        return posts