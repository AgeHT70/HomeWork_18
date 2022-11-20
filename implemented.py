from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO

from app.service.director import DirectorService
from app.service.genre import GenreService
from app.service.movie import MovieService

from setup_db import db

movie_dao = MovieDAO(session=db.session)
movie_service = MovieService(dao=movie_dao)

director_dao = DirectorDAO(session=db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(session=db.session)
genre_service = GenreService(dao=genre_dao)