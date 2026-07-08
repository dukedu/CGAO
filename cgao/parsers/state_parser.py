from __future__ import annotations

import json
import re

from cgao.parsers.detail_parser import DetailParser


class StateParser:

    @staticmethod
    def parse(html: str):

        state = StateParser.extract(html)

        return StateParser.build(state)

    @staticmethod
    def extract(html: str):

        pattern = re.compile(

            r"window\.__INITIAL_STATE__\s*=\s*(\{.*?\})\s*</script>",

            re.S,

        )

        match = pattern.search(html)

        if match is None:

            raise RuntimeError(

                "__INITIAL_STATE__ not found."

            )

        text = match.group(1)

        text = text.replace(

            ":undefined",

            ":null",

        )

        text = text.replace(

            ":NaN",

            ":null",

        )

        text = text.replace(

            ":Infinity",

            ":null",

        )

        return json.loads(text)

    @staticmethod
    def build(state):

        note_map = state["note"]["noteDetailMap"]

        note = next(

            iter(

                note_map.values()

            )

        )["note"]

        return DetailParser.parse(note)