from dataclasses import dataclass
from dataclasses import asdict


@dataclass
class Post:

    note_id: str

    xsec_token: str

    title: str

    author: str

    like_count: int

    url: str

    def to_dict(self):

        return asdict(self)