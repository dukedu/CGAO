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

        text = StateParser._extract_state(html)

        text = StateParser._normalize_js_value(text)

        try:

            return json.loads(text)

        except json.JSONDecodeError:

            decoder = json.JSONDecoder()

            state, _ = decoder.raw_decode(text)

            return state

    @staticmethod
    def _extract_state(html: str) -> str:

        marker = "window.__INITIAL_STATE__"

        start = html.find(marker)

        if start < 0:

            raise RuntimeError("__INITIAL_STATE__ not found")

        brace_start = html.find("{", start)

        if brace_start < 0:

            raise RuntimeError("__INITIAL_STATE__ object not found")

        depth = 0

        in_string = False

        quote = ""

        escape = False

        for index in range(
            brace_start,
            len(html),
        ):

            char = html[index]

            if in_string:

                if escape:

                    escape = False

                    continue

                if char == "\\":

                    escape = True

                    continue

                if char == quote:

                    in_string = False

                    quote = ""

                continue

            if char in ('"', "'"):

                in_string = True

                quote = char

                continue

            if char == "{":

                depth += 1

                continue

            if char == "}":

                depth -= 1

                if depth == 0:

                    return html[
                        brace_start : index + 1
                    ]

        raise RuntimeError("__INITIAL_STATE__ object incomplete")

    @staticmethod
    def _normalize_js_value(text: str) -> str:

        text = re.sub(
            r"(?<![A-Za-z0-9_$\"'])undefined(?![A-Za-z0-9_$\"'])",
            "null",
            text,
        )

        text = re.sub(
            r"(?<![A-Za-z0-9_$\"'])NaN(?![A-Za-z0-9_$\"'])",
            "null",
            text,
        )

        text = re.sub(
            r"(?<![A-Za-z0-9_$\"'])Infinity(?![A-Za-z0-9_$\"'])",
            "null",
            text,
        )

        return text

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

                except RuntimeError:

                    pass

        elif isinstance(obj, list):

            for item in obj:

                try:

                    return StateParser._find(item)

                except RuntimeError:

                    pass

        raise RuntimeError("Note object not found.")
