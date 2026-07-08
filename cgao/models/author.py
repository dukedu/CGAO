from dataclasses import dataclass


@dataclass(slots=True)
class Author:

    author_id: str

    nickname: str

    avatar: str = ""

    xsec_token: str = ""