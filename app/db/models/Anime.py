from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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
            return self.id == other.id
        return False


Base = declarative_base()


class AnimeModel(Base):
    __tablename__ = 'anime'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    release_date = Column(DateTime)
    watched = Column(Boolean)
