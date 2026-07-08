from __future__ import annotations

from cgao.services.crawler_service import CrawlerService
from cgao.services.database_service import DatabaseService
from cgao.services.detail_collector import DetailCollector
from cgao.services.export_service import ExportService


class Pipeline:

    def __init__(self):

        self.crawler = CrawlerService()

        self.database = DatabaseService()

        self.exporter = ExportService()

    def collect(
        self,
        keyword: str,
        limit: int = 100,
        csv: str | None = None,
        json: str | None = None,
    ):

        try:

            posts = self.crawler.collect(
                keyword=keyword,
                limit=limit,
            )

            collector = DetailCollector(
                self.crawler.crawler
            )

            results = []

            for post in posts:

                try:

                    result = collector.collect(post)

                except Exception as e:

                    print(e)

                    continue

                self.database.save(result)

                results.append(result.post)

            if csv:

                self.exporter.csv_export(
                    results,
                    csv,
                )

            if json:

                self.exporter.json_export(
                    results,
                    json,
                )

            return results

        finally:

            self.database.close()

            self.crawler.close()