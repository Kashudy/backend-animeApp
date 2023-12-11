from dataclasses import dataclass
from datetime import datetime


@dataclass
class Anime:
    id: int
    title: str
    release_date: datetime
    watched: bool = False

    def __post_init__(self):
        self.watched = False

    def __eq__(self, other):
        if isinstance(other, Anime):
            return self.id == other.id and self.title == other.title and self.release_date == other.release_date
        return False
