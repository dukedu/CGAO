from __future__ import annotations

from cgao.models import Author


class AuthorParser:

    @staticmethod
    def parse(note: dict) -> Author:

        user = note["user"]

        return Author(

            author_id=user.get("userId", ""),

            nickname=user.get("nickname", ""),

            avatar=user.get("avatar", ""),

            xsec_token=user.get("xsecToken", ""),

            description=user.get("desc", ""),

            gender=str(user.get("gender", "")),

        )