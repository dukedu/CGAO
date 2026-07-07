from dataclasses import dataclass


@dataclass
class Post:
    note_id: str
    xsec_token: str

    title: str
    author: str

    like_count: int

    url: str