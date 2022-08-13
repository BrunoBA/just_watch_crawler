from just_watch_crawler.movie_search.MovieSearch import MovieSearch


title = input("Please inform the movie name:\n")
movie_search = MovieSearch()
movies = movie_search.search_by_title(title)
# just_watch = JustWatch(country='US')
# the_matrix = just_watch.search_title_id(query='Batman')
# json_object = Formatter(the_matrix) 

# print(json_object)


# data = Formatter(just_watch.get_title(title_id=56184, content_type='movie'))
print(movies)
