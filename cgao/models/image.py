from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Image:

    note_id: str = ""

    url: str = ""

    width: int = 0

    height: int = 0

    file_id: str = ""

    format: str = ""

    size: int = 0

    order: int = 0

    def resolution(self):

        return (

            self.width,

            self.height,

        )

    @property

    def aspect_ratio(self):

        if self.height == 0:

            return 0

        return self.width / self.height

    def to_dict(self):

        return {

            "note_id": self.note_id,

            "url": self.url,

            "width": self.width,

            "height": self.height,

            "file_id": self.file_id,

            "format": self.format,

            "size": self.size,

            "order": self.order,

        }