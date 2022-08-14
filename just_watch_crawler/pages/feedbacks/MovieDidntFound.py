

from just_watch_crawler.pages.feedbacks.Feedback import Feedback


class MovieDidntFound(Feedback):
    def __init__(self, movie) -> None:
        self.movie = movie

    def feedback(self):
        print("""

** {} is not available ):

""".format(self.movie.original_title))
        