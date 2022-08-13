from just_watch_crawler.country_fetch.CountryFetch import CountryFetch
from just_watch_crawler.movie_search.MovieSearch import MovieSearch
from just_watch_crawler.pages.Menu import Menu

title = input("Please inform the movie name:\n")
movie_search = MovieSearch()
movies = movie_search.search_by_title(title)

menu = Menu(movies)
movie_id = menu.select_movie()

if (movie_id != 0):
    movieSearch = CountryFetch()
    countries_available = movieSearch.get_countries_by(movie_id)

    print("The movie is available in: \n")
    for country in countries_available:
        print(country)

