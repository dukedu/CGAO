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

        user = note.get("user") or {}

        interact = note.get("interactInfo") or {}

        post = Post(
            note_id=DetailParser._str(
                note.get("noteId")
                or note.get("id")
            ),
            title=DetailParser._str(
                note.get("title")
                or note.get("displayTitle")
            ),
            content=DetailParser._str(
                note.get("desc")
            ),
            author_id=DetailParser._str(
                user.get("userId")
            ),
            author=DetailParser._str(
                user.get("nickname")
                or user.get("nickName")
            ),
            publish_time=DetailParser._time(
                note.get("time")
                or note.get("lastUpdateTime")
            ),
            ip_location=DetailParser._str(
                note.get("ipLocation")
            ),
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
            xsec_token=DetailParser._str(
                note.get("xsecToken")
            ),
        )

        author = Author(
            author_id=DetailParser._str(
                user.get("userId")
            ),
            nickname=DetailParser._str(
                user.get("nickname")
                or user.get("nickName")
            ),
            avatar=DetailParser._str(
                user.get("avatar")
                or user.get("image")
                or user.get("images")
            ),
            xsec_token=DetailParser._str(
                user.get("xsecToken")
            ),
            follower_count=DetailParser._int(
                user.get("fans")
                or user.get("followerCount")
                or user.get("fansCount")
            ),
            following_count=DetailParser._int(
                user.get("follows")
                or user.get("followingCount")
                or user.get("followsCount")
            ),
            note_count=DetailParser._int(
                user.get("notes")
                or user.get("noteCount")
            ),
            liked_count=DetailParser._int(
                user.get("liked")
                or user.get("likedCount")
            ),
            description=DetailParser._str(
                user.get("desc")
                or user.get("description")
            ),
            gender=DetailParser._str(
                user.get("gender")
            ),
            ip_location=DetailParser._str(
                user.get("ipLocation")
            ),
            verified=bool(
                user.get("verified")
                or user.get("redOfficialVerify")
            ),
        )

        images = []

        for idx, img in enumerate(
            note.get("imageList") or []
        ):

            url = DetailParser._image_url(img)

            images.append(
                Image(
                    note_id=post.note_id,
                    url=url,
                    width=DetailParser._int(
                        img.get("width")
                    ),
                    height=DetailParser._int(
                        img.get("height")
                    ),
                    file_id=DetailParser._str(
                        img.get("fileId")
                    ),
                    format=DetailParser._str(
                        img.get("format")
                    ),
                    size=DetailParser._int(
                        img.get("size")
                    ),
                    order=idx,
                )
            )

        tags = []

        for item in note.get("tagList") or []:

            name = DetailParser._str(
                item.get("name")
            )

            if not name:

                continue

            tags.append(
                Tag(
                    tag_id=DetailParser._int(
                        item.get("id")
                    ),
                    name=name,
                )
            )

        return DetailResult(
            post=post,
            author=author,
            images=images,
            tags=tags,
        )

    @staticmethod
    def _image_url(img: dict) -> str:

        if not isinstance(img, dict):

            return ""

        if img.get("urlDefault"):

            return DetailParser._str(
                img.get("urlDefault")
            )

        if img.get("url"):

            return DetailParser._str(
                img.get("url")
            )

        info_list = img.get("infoList") or []

        if isinstance(info_list, list):

            for item in reversed(info_list):

                if isinstance(item, dict) and item.get("url"):

                    return DetailParser._str(
                        item.get("url")
                    )

        return ""

    @staticmethod
    def _time(ts):

        if not ts:

            return ""

        try:

            value = int(ts)

            if value > 100000000000:

                value = value / 1000

            return datetime.fromtimestamp(
                value
            ).strftime("%Y-%m-%d %H:%M:%S")

        except Exception:

            return ""

    @staticmethod
    def _int(v):

        if v is None:

            return 0

        if isinstance(v, bool):

            return int(v)

        if isinstance(v, int):

            return v

        if isinstance(v, float):

            return int(v)

        s = str(v)

        multiplier = 1

        if "万" in s:

            multiplier = 10000

        s = (
            s.replace(",", "")
            .replace("+", "")
            .replace("万", "")
            .strip()
        )

        try:

            return int(float(s) * multiplier)

        except Exception:

            return 0

    @staticmethod
    def _str(v):

        if v is None:

            return ""

        return str(v)
