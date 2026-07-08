from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Comment:

    comment_id: str = ""

    note_id: str = ""

    author_id: str = ""

    author: str = ""

    content: str = ""

    publish_time: str = ""

    like_count: int = 0

    reply_count: int = 0

    ip_location: str = ""

    def to_dict(self):

        return {

            "comment_id": self.comment_id,

            "note_id": self.note_id,

            "author_id": self.author_id,

            "author": self.author,

            "content": self.content,

            "publish_time": self.publish_time,

            "like_count": self.like_count,

            "reply_count": self.reply_count,

            "ip_location": self.ip_location,

        }