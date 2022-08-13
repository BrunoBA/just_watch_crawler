from justwatch import JustWatch

class MovieSearch:
    def __init__(self) -> None:
        self.just_watch = JustWatch(country='US')

    def search_by_title(self, title: str):
        try:
            possible_movies = self.just_watch.search_title_id(query=title)
            return possible_movies
        except:
            return []
        