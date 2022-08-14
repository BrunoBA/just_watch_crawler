from just_watch_crawler.movie_search.MovieSearch import MovieSearch
from just_watch_crawler.pages.Menu import Menu

class MovieSelect:
    def __init__(self) -> None:
        pass

    def choose_movie(self):
        title = input("Please inform the movie name:\n")
        movie_search = MovieSearch()
        movies = movie_search.search_by_title(title)

        menu = Menu(movies)
        movie = menu.select_movie()

        return movie
