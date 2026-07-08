from __future__ import annotations

from datetime import datetime

from cgao.models import DetailResult
from cgao.models import Image
from cgao.models import Post
from cgao.models import Tag

from .author_parser import AuthorParser


class DetailParser:

    @staticmethod
    def parse(note: dict) -> DetailResult:

        interact = note.get(

            "interactInfo",

            {},

        )

        post = Post(

            note_id=note.get(

                "noteId",

                "",

            ),

            title=note.get(

                "title",

                "",

            ),

            content=note.get(

                "desc",

                "",

            ),

            author_id=note["user"].get(

                "userId",

                "",

            ),

            author=note["user"].get(

                "nickname",

                "",

            ),

            publish_time=DetailParser._time(

                note.get(

                    "time",

                    0,

                )

            ),

            ip_location=note.get(

                "ipLocation",

                "",

            ),

            like_count=int(

                interact.get(

                    "likedCount",

                    0,

                )

            ),

            collect_count=int(

                interact.get(

                    "collectedCount",

                    0,

                )

            ),

            comment_count=int(

                interact.get(

                    "commentCount",

                    0,

                )

            ),

            share_count=int(

                interact.get(

                    "shareCount",

                    0,

                )

            ),

            xsec_token=note.get(

                "xsecToken",

                "",

            ),

        )

        author = AuthorParser.parse(

            note

        )

        images = []

        for idx, img in enumerate(

            note.get(

                "imageList",

                [],

            )

        ):

            images.append(

                Image(

                    note_id=post.note_id,

                    url=img.get(

                        "urlDefault",

                        "",

                    ),

                    width=img.get(

                        "width",

                        0,

                    ),

                    height=img.get(

                        "height",

                        0,

                    ),

                    order=idx,

                )

            )

        tags = []

        for t in note.get(

            "tagList",

            [],

        ):

            tags.append(

                Tag(

                    name=t.get(

                        "name",

                        "",

                    )

                )

            )

        return DetailResult(

            post=post,

            author=author,

            images=images,

            tags=tags,

        )

    @staticmethod
    def _time(ts):

        if not ts:

            return ""

        return datetime.fromtimestamp(

            ts / 1000

        ).strftime(

            "%Y-%m-%d %H:%M:%S"

        )