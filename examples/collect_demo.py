from cgao.services.crawler_service import CrawlerService

crawler = CrawlerService()

posts = crawler.collect(

    keyword="DeepSeek",

    limit=20,

)

print()

print(len(posts))

print(posts[0])