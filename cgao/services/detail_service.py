from cgao.parsers.state_parser import StateParser


class DetailService:

    def parse(self, html):

        return StateParser.parse(html)