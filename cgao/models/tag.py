from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Tag:

    tag_id: int = 0

    name: str = ""

    use_count: int = 0

    view_count: int = 0

    def to_dict(self):

        return {

            "tag_id": self.tag_id,

            "name": self.name,

            "use_count": self.use_count,

            "view_count": self.view_count,

        }