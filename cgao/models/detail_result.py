from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from cgao.models.author import Author
from cgao.models.comment import Comment
from cgao.models.image import Image
from cgao.models.post import Post
from cgao.models.tag import Tag


@dataclass(slots=True)
class DetailResult:

    post: Post

    author: Author

    images: list[Image] = field(

        default_factory=list

    )

    tags: list[Tag] = field(

        default_factory=list

    )

    comments: list[Comment] = field(

        default_factory=list

    )

    def to_dict(self):

        return {

            "post": self.post.to_dict(),

            "author": self.author.to_dict(),

            "images": [

                i.to_dict()

                for i in self.images

            ],

            "tags": [

                t.to_dict()

                for t in self.tags

            ],

            "comments": [

                c.to_dict()

                for c in self.comments

            ],

        }