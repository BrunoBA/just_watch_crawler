from typing import Optional
from just_watch_crawler.model.Movie import Movie
from just_watch_crawler.movie_search.MovieSearch import MovieSearch


class Menu:
    def __init__(self, movies) -> None:
        self.movies = movies
        self.movie_ids = []
        self.titles = []

    def __get_movie_id_by_numer(self, index: int) -> int:
        return self.movies[self.titles[index - 1]]

    def __print_option(self, value, name) -> None:
        print("{:^2} - {}".format(value, name))

    def ask_movie(self) -> int:
        option = None
        tried = False

        movie_range = range(0, len(self.movie_ids) + 1)
        while option not in movie_range:
            self.show_options()
            self.__print_option(0, "To Exit")
            if (tried):
                print("PLEASE CHOOSE A VALID OPTION \n")
            option = int(input("\nPlease choose a movie number: \n"))

            if (option == 0):
                return 0
            tried = True

        return int(option)

    def load_movies(self) -> None:
        for movie_name in self.movies:
            self.titles.append(movie_name)

        self.titles.sort()
        for title in self.titles:
            movie_id = self.movies[title]
            self.movie_ids.append(int(movie_id))

    def show_options(self) -> None:
        for index, title in enumerate(self.titles):
            movie_and_register = "{} (#{})".format(title, self.movies[title])
            self.__print_option(index + 1, movie_and_register)

    def select_movie(self) -> Optional[Movie]:
        self.load_movies()
        anwser = "no"
        while anwser.lower() != "yes":
            movie_number = self.ask_movie()
            
            if (movie_number == 0):
                return None

            movie_search = MovieSearch()
            movie_id = self.__get_movie_id_by_numer(movie_number)
            movie = movie_search.search_by_id(movie_id)

            print(Movie(movie))

            anwser = input("Is this movie you're looking for? (yes/no)\n")
    
        return Movie(movie)
       
        
        