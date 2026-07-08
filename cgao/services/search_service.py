from __future__ import annotations

from cgao.services.crawler_service import CrawlerService


class SearchService:

    def __init__(self):

        self.crawler = CrawlerService()

    def search(

        self,

        keyword,

        limit=100,

    ):

        return self.crawler.collect(

            keyword,

            limit,

        )