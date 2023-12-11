import Anime


class getAnime_UnitTest:

    db = None

    id: int = 1
    retrieved_anime: Anime = None

    def setUp(self):
        self.retrieved_anime = db.getAnime(id)

    def getExistingAnimeFromDB(self):

        expectedAnime: Anime = Anime(id=1, title="Naruto",
                                     release_date='2020-11-10 18:30:00')

        assert (self.retrieved_anime == expectedAnime)
