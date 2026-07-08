from __future__ import annotations

from cgao.services.crawler_service import CrawlerService
from cgao.services.export_service import ExportService


class Pipeline:

    def __init__(self):

        self.crawler = CrawlerService()

        self.exporter = ExportService()

    def collect(

        self,

        keyword,

        limit=100,

        csv=None,

        json=None,

    ):

        posts = self.crawler.collect(

            keyword,

            limit,

        )

        if csv:

            self.exporter.csv_export(

                posts,

                csv,

            )

        if json:

            self.exporter.json_export(

                posts,

                json,

            )

        return posts