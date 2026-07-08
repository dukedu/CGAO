from dataclasses import dataclass, field

from cgao.models.author import Author
from cgao.models.image import Image
from cgao.models.post import Post
from cgao.models.tag import Tag


@dataclass(slots=True)
class DetailResult:

    post: Post

    author: Author

    images: list[Image] = field(default_factory=list)

    tags: list[Tag] = field(default_factory=list)