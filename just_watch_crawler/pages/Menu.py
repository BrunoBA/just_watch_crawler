

class Menu:
    def __init__(self, movies) -> None:
        self.movies = movies
        self.movie_ids = []
        self.titles = []

    def __print_option(self, value, name) -> None:
        print("{:^7} - {:^3}".format(value, name))

    def ask_movie(self) -> int:
        option = None
        tryed = False
        while option not in self.movie_ids:
            self.show_options()
            
            self.__print_option(0, "To Exit")
            if (tryed):
                print("PLEASE CHOOSE A VALID OPTION \n")
            option = int(input("Please choose a movie id: \n"))

            if (option == 0):
                return 0
            tryed = True

        return int(option)

    def load_movies(self) -> None:
        for movie_name in self.movies:
            self.titles.append(movie_name)

        self.titles.sort()
        for title in self.titles:
            movie_id = self.movies[title]
            self.movie_ids.append(int(movie_id))

    def show_options(self) -> None:
        for title in self.titles:
            self.__print_option(self.movies[title], title)

    def select_movie(self) -> int:
       self.load_movies()
       return self.ask_movie()
       
        
        