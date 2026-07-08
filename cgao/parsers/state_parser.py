import json
import re

from cgao.models import (
    Author,
    DetailResult,
    Image,
    Post,
    Tag,
)


class StateParser:

    @staticmethod
    def parse(html: str) -> DetailResult:

        state = StateParser._load_state(html)

        return StateParser._build_result(state)

    @staticmethod
    def _load_state(html):

        m = re.search(

            r"window\.__INITIAL_STATE__\s*=\s*(\{.*?\})\s*</script>",

            html,

            re.S,

        )

        if m is None:

            raise RuntimeError(

                "__INITIAL_STATE__ not found"

            )

        text = m.group(1)

        text = text.replace(":undefined", ":null")

        text = text.replace(":NaN", ":null")

        text = text.replace(":Infinity", ":null")

        return json.loads(text)

    @staticmethod
    def _build_result(state):

        note_store = state["note"]["noteDetailMap"]

        note = next(iter(note_store.values()))["note"]

        post = Post(

            note_id=note["noteId"],

            title=note["title"],

            content=note["desc"],

            author_id=note["user"]["userId"],

            author=note["user"]["nickname"],

            ip_location=note.get(

                "ipLocation",

                ""

            ),

            like_count=int(

                note["interactInfo"]["likedCount"]

            ),

            collect_count=int(

                note["interactInfo"]["collectedCount"]

            ),

            comment_count=int(

                note["interactInfo"]["commentCount"]

            ),

            share_count=int(

                note["interactInfo"]["shareCount"]

            ),

            xsec_token=note["xsecToken"],

        )

        author = Author(

            author_id=note["user"]["userId"],

            nickname=note["user"]["nickname"],

            avatar=note["user"]["avatar"],

            xsec_token=note["user"]["xsecToken"],

        )

        images = []

        for img in note.get(

            "imageList",

            []

        ):

            images.append(

                Image(

                    note_id=note["noteId"],

                    url=img["urlDefault"],

                    width=img["width"],

                    height=img["height"],

                )

            )

        tags = []

        for tag in note.get(

            "tagList",

            []

        ):

            tags.append(

                Tag(

                    name=tag["name"]

                )

            )

        return DetailResult(

            post=post,

            author=author,

            images=images,

            tags=tags,

        )