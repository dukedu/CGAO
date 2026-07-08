from dataclasses import dataclass, field


@dataclass
class Detail:

    note_id: str = ""

    title: str = ""

    content: str = ""

    author: str = ""

    author_id: str = ""

    publish_time: str = ""

    ip_location: str = ""

    like_count: int = 0

    collect_count: int = 0

    comment_count: int = 0

    share_count: int = 0

    tags: list[str] = field(default_factory=list)

    images: list[str] = field(default_factory=list)

    url: str = ""