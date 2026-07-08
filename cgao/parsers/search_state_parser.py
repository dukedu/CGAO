from __future__ import annotations

import json
import re

from cgao.models import Post


class SearchStateParser:

    @staticmethod
    def parse(html: str) -> list[Post]:

        state = SearchStateParser._load_state(html)

        posts = {}

        SearchStateParser._walk(state, posts)

        return list(posts.values())

    @staticmethod
    def _load_state(html: str):

        m = re.search(
            r"window\.__INITIAL_STATE__\s*=\s*(\{.*?\})\s*</script>",
            html,
            re.S,
        )

        if not m:
            raise RuntimeError("__INITIAL_STATE__ not found")

        text = m.group(1)

        decoder = json.JSONDecoder()

        state, _ = decoder.raw_decode(text)

        return state

    @staticmethod
    def _walk(obj, posts):

        if isinstance(obj, dict):

            SearchStateParser._try_parse_note(
                obj,
                posts,
            )

            for value in obj.values():

                SearchStateParser._walk(
                    value,
                    posts,
                )

        elif isinstance(obj, list):

            for item in obj:

                SearchStateParser._walk(
                    item,
                    posts,
                )

    @staticmethod
    def _try_parse_note(obj, posts):

        note_id = obj.get("id")

        note_card = obj.get("noteCard")

        if not note_id:

            return

        if not isinstance(note_card, dict):

            return

        user = note_card.get("user", {})

        cover = note_card.get("cover", {})

        interact = note_card.get("interactInfo", {})

        post = Post(

            note_id=note_id,

            xsec_token=obj.get("xsecToken", ""),

            title=(
                note_card.get("displayTitle")
                or note_card.get("title")
                or ""
            ),

            author=user.get(
                "nickname",
                "",
            ),

            author_id=user.get(
                "userId",
                "",
            ),

            like_count=SearchStateParser._int(
                interact.get("likedCount")
            ),

            comment_count=SearchStateParser._int(
                interact.get("commentCount")
            ),

            collect_count=SearchStateParser._int(
                interact.get("collectedCount")
            ),

            share_count=SearchStateParser._int(
                interact.get("shareCount")
            ),

        )

        if hasattr(post, "cover"):

            try:

                post.cover = (
                    cover.get("urlDefault")
                    or cover.get("url")
                    or ""
                )

            except Exception:

                pass

        posts[note_id] = post

    @staticmethod
    def _int(value):

        if value is None:

            return 0

        if isinstance(value, int):

            return value

        if isinstance(value, float):

            return int(value)

        s = str(value)

        s = (
            s.replace(",", "")
            .replace("+", "")
            .replace("万", "")
            .strip()
        )

        try:

            return int(float(s))

        except Exception:

            return 0