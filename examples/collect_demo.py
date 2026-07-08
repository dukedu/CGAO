from cgao.services import (

    CrawlerService,

    ExportService,

)

crawler = CrawlerService()

export = ExportService()

posts = crawler.collect(

    keyword="DeepSeek",

    limit=50,

)

export.export_csv(

    posts,

    "data/raw/DeepSeek.csv",

)

export.export_json(

    posts,

    "data/raw/DeepSeek.json",

)

print()

print(f"Collected: {len(posts)}")