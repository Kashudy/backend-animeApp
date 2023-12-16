from abc import ABC, abstractmethod
from db.models.Anime import Anime as AnimeModel


class DatabaseInterface(ABC):
    @abstractmethod
    def get_anime_by_id(self, key: int) -> str:
        pass

    @abstractmethod
    def set_anime(self, anime: AnimeModel) -> None:
        pass

    @abstractmethod
    def delete_anime_by_id(self, key: int) -> None:
        pass

    @abstractmethod
    def update_anime_watched_by_id(self, key: int) -> None:
        pass

    @abstractmethod
    def get_all_anime(self) -> str:
        pass
