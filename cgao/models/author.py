from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Author:

    author_id: str = ""

    nickname: str = ""

    avatar: str = ""

    xsec_token: str = ""

    follower_count: int = 0

    following_count: int = 0

    note_count: int = 0

    liked_count: int = 0

    description: str = ""

    gender: str = ""

    ip_location: str = ""

    verified: bool = False

    def profile_url(self):

        if not self.author_id:

            return ""

        return (

            "https://www.xiaohongshu.com/user/profile/"

            f"{self.author_id}"

        )

    def to_dict(self):

        return {

            "author_id": self.author_id,

            "nickname": self.nickname,

            "avatar": self.avatar,

            "xsec_token": self.xsec_token,

            "follower_count": self.follower_count,

            "following_count": self.following_count,

            "note_count": self.note_count,

            "liked_count": self.liked_count,

            "description": self.description,

            "gender": self.gender,

            "ip_location": self.ip_location,

            "verified": self.verified,

        }