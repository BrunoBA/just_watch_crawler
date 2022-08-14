from just_watch_crawler.country_fetch.CountryFetch import CountryFetch
from just_watch_crawler.pages.MovieSelect import MovieSelect
from just_watch_crawler.pages.feedbacks.MovieFound import MovieFound
from just_watch_crawler.pages.feedbacks.MovieDidntFound import MovieDidntFound

exit = False
while not exit:
    movie_select = MovieSelect()
    movie = movie_select.choose_movie()

    if movie is not None:
        movieSearch = CountryFetch()
        countries_available = movieSearch.get_countries_by(movie.id)

        if len(countries_available) == 0:
            MovieDidntFound(movie).feedback()
        else:
            MovieFound(movie, countries_available).feedback()
            
    else:
        exit = True

