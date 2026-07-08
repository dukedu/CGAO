from cgao.services.crawler_service import CrawlerService
from cgao.exporters.csv_exporter import CSVExporter

service = CrawlerService()

posts = service.search_and_collect(
    keyword="DeepSeek",
    limit=10
)

CSVExporter().export(
    posts,
    "data/raw/DeepSeek.csv"
)