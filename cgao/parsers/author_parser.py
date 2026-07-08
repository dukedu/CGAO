from cgao.models import Author


class AuthorParser:

    @staticmethod
    def parse(note: dict) -> Author:

        user = note["user"]

        return Author(

            author_id=user["userId"],

            nickname=user["nickname"],

            avatar=user.get("avatar", ""),

            xsec_token=user.get("xsecToken", "")

        )