import i_db as Database_interface
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from db.models.Anime import Anime as AnimeModel

Base = declarative_base()


class DatabaseError(Exception):
    pass


class db_sqlAlchemy(Database_interface):

    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def handle_db_error(self, error_msg: str):
        raise DatabaseError(f"Database error: {error_msg}")

    def get_anime_by_id(self, key: int) -> AnimeModel:
        try:
            with self.Session() as session:
                anime_model = session.query(
                    AnimeModel).filter_by(id=key).first()
                if anime_model:
                    return anime_model
                self.handle_db_error(f"Anime with id {key} not found")
        except Exception as e:
            self.handle_db_error(str(e))

    def set_anime(self, new_anime: AnimeModel) -> None:
        try:
            with self.Session() as session:
                session.add(new_anime)
                session.commit()
        except IntegrityError as e:
            self.handle_db_error(str(e))

    def delete_anime_by_id(self, key: int) -> None:
        try:
            with self.Session() as session:
                anime_model = session.query(
                    AnimeModel).filter_by(id=key).first()
                if anime_model:
                    session.delete(anime_model)
                    session.commit()
                else:
                    self.handle_db_error(f"Anime with id {key} not found")
        except Exception as e:
            self.handle_db_error(str(e))

    def update_anime_watched_by_id(self, key: int) -> None:
        try:
            with self.Session() as session:
                anime_model = session.query(
                    AnimeModel).filter_by(id=key).first()
                if anime_model:
                    anime_model.watched = True
                    session.commit()
                else:
                    self.handle_db_error(f"Anime with id {key} not found")
        except Exception as e:
            self.handle_db_error(str(e))

    def get_all_anime(self) -> list[AnimeModel]:
        try:
            with self.Session() as session:
                anime_models = session.query(AnimeModel).all()
                return anime_models
        except Exception as e:
            self.handle_db_error(str(e))
