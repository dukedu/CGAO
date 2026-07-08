from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Post:

    note_id: str = ""

    title: str = ""

    content: str = ""

    author_id: str = ""

    author: str = ""

    publish_time: str = ""

    ip_location: str = ""

    like_count: int = 0

    collect_count: int = 0

    comment_count: int = 0

    share_count: int = 0

    xsec_token: str = ""

    def detail_url(self) -> str:

        if not self.note_id:

            return ""

        if self.xsec_token:

            return (
                "https://www.xiaohongshu.com/explore/"
                f"{self.note_id}"
                f"?xsec_token={self.xsec_token}"
            )

        return (
            "https://www.xiaohongshu.com/explore/"
            f"{self.note_id}"
        )

    @property
    def engagement(self):

        return (

            self.like_count

            + self.collect_count

            + self.comment_count

            + self.share_count

        )

    def to_dict(self):

        return {

            "note_id": self.note_id,

            "title": self.title,

            "content": self.content,

            "author_id": self.author_id,

            "author": self.author,

            "publish_time": self.publish_time,

            "ip_location": self.ip_location,

            "like_count": self.like_count,

            "collect_count": self.collect_count,

            "comment_count": self.comment_count,

            "share_count": self.share_count,

            "xsec_token": self.xsec_token,

        }