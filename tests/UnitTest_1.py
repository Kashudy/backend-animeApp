import Anime
import pytest
from db.exc import NoResultFound, IntegrityError
import i_db as Database

db: Database = Database.Database()


class GET_Anime_UnitTest:

    retrieved_anime: Anime = Anime(id=1, title="Naruto",
                                   release_date='2020-11-10 18:30:00')

    def GET_ExistingAnimeFromDB(self):

        expectedAnime: Anime = Anime(id=1, title="Naruto",
                                     release_date='2020-11-10 18:30:00')

        assert (self.retrieved_anime == expectedAnime)

    def GET_NonExistentAnimeFromDB(self):
        with pytest.raises(NoResultFound):
            db.get_anime_by_id(99999)


class POST_Anime_UnitTest:

    new_anime: Anime = Anime(id=1, title="Naruto",
                             release_date='2020-11-10 18:30:00')

    def tearDown(self):
        db.dev.clean()

    def POST_NonExistentAnimeFromDB(self):
        db.post_anime(new_anime)
        retrieved_anime: Anime = db.get_anime_by_id(new_anime.id)
        assert (retrieved_anime == new_anime)

    def POST_ExistingAnimeFromDB(self):
        db.post_anime(new_anime)
        with pytest.raises(IntegrityError):
            db.post_anime(new_anime)
