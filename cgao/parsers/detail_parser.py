from __future__ import annotations

from datetime import datetime

from cgao.models import (
    Author,
    DetailResult,
    Image,
    Post,
    Tag,
)


class DetailParser:

    @staticmethod
    def parse(note: dict) -> DetailResult:

        user = note.get("user", {})
        interact = note.get("interactInfo", {})

        post = Post(
            note_id=note.get("noteId", ""),
            title=note.get("title", ""),
            content=note.get("desc", ""),
            author_id=user.get("userId", ""),
            author=user.get("nickname", ""),
            publish_time=DetailParser._time(
                note.get("time")
                or note.get("lastUpdateTime")
            ),
            ip_location=note.get("ipLocation", ""),
            like_count=DetailParser._int(
                interact.get("likedCount")
            ),
            collect_count=DetailParser._int(
                interact.get("collectedCount")
            ),
            comment_count=DetailParser._int(
                interact.get("commentCount")
            ),
            share_count=DetailParser._int(
                interact.get("shareCount")
            ),
            xsec_token=note.get("xsecToken", ""),
        )

        author = Author(
            user_id=user.get("userId", ""),
            nickname=user.get("nickname", ""),
            avatar=user.get("image", ""),
            desc=user.get("desc", ""),
            follows=DetailParser._int(
                user.get("follows")
            ),
            fans=DetailParser._int(
                user.get("fans")
            ),
            notes=DetailParser._int(
                user.get("notes")
            ),
        )

        images = []

        for idx, img in enumerate(
            note.get("imageList", [])
        ):

            url = (
                img.get("urlDefault")
                or img.get("url")
                or img.get("infoList", [{}])[-1].get("url", "")
            )

            images.append(
                Image(
                    note_id=post.note_id,
                    url=url,
                    width=img.get("width", 0),
                    height=img.get("height", 0),
                    order=idx,
                )
            )

        tags = []

        for t in note.get("tagList", []):

            tags.append(
                Tag(
                    name=t.get("name", "")
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

        try:
            return datetime.fromtimestamp(
                int(ts) / 1000
            ).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            return ""

    @staticmethod
    def _int(v):

        if v is None:
            return 0

        if isinstance(v, int):
            return v

        if isinstance(v, float):
            return int(v)

        s = str(v)

        s = (
            s.replace(",", "")
             .replace("万", "")
             .replace("+", "")
             .strip()
        )

        try:
            return int(float(s))
        except Exception:
            return 0