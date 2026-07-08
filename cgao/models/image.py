from dataclasses import dataclass


@dataclass(slots=True)
class Image:

    note_id: str

    url: str

    width: int = 0

    height: int = 0