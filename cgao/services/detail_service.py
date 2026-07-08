from __future__ import annotations

from cgao.parsers import StateParser


class DetailService:

    @staticmethod
    def parse(html):

        return StateParser.parse(html)