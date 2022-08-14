
from just_watch_crawler.model.Cast import Cast


class Movie:
    def __init__(self, movie) -> None:
        self.id = movie['id']
        self.short_description = movie['short_description']
        self.original_release_year = movie['original_release_year']
        self.object_type = movie['object_type']
        self.original_title = movie['original_title']
        self.__initialize_cast(movie)

    def __initialize_cast(self, movie) -> None:
        self.cast = []
        if 'credits' not in movie:
            return
        for index, credit in enumerate(movie['credits']):
            self.cast.append(Cast(credit))
            if (index == 2):
                return

    def __group_cast(self) -> str:
        cast_str = ""
        for cast in self.cast:
            cast_str += str(cast) + "\n"

        return cast_str

    def __str__(self) -> str:
        return """
{} ({})

{}


{}
        """.format(
            self.original_title,
            self.original_release_year,
            self.short_description,            
            self.__group_cast(),
        )