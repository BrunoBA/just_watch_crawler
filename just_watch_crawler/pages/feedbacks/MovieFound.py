
from just_watch_crawler.pages.feedbacks.Feedback import Feedback


class MovieFound(Feedback):
    def __init__(self, movie, countries_available) -> None:
        self.movie = movie
        self.countries_available = countries_available

    def feedback(self):
        print("""
        
** {} is available in: \n""".format(self.movie.original_title))
        for country in self.countries_available:
            print(country)
