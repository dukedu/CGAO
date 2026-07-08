from __future__ import annotations

import json
import re

from cgao.parsers.detail_parser import DetailParser


class StateParser:

    @staticmethod
    def parse(html: str):

        state = StateParser._load(html)

        return StateParser._find(state)

    @staticmethod
    def _load(html: str):

        m = re.search(
            r"window\.__INITIAL_STATE__\s*=\s*(\{.*?\})\s*</script>",
            html,
            re.S,
        )

        if not m:
            raise RuntimeError("__INITIAL_STATE__ not found")

        text = m.group(1)

        try:
            return json.loads(text)
        except json.JSONDecodeError:

            decoder = json.JSONDecoder()

            state, _ = decoder.raw_decode(text)

            return state

    @staticmethod
    def _find(obj):

        if isinstance(obj, dict):

            if "noteId" in obj and "user" in obj:

                return DetailParser.parse(obj)

            if "note" in obj and isinstance(obj["note"], dict):

                note = obj["note"]

                if "noteId" in note:

                    return DetailParser.parse(note)

            for value in obj.values():

                try:

                    return StateParser._find(value)

                except Exception:

                    pass

        elif isinstance(obj, list):

            for item in obj:

                try:

                    return StateParser._find(item)

                except Exception:

                    pass

        raise RuntimeError("Note object not found.")