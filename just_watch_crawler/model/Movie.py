
from just_watch_crawler.model.Cast import Cast


class Movie:
    def __init__(self, movie) -> None:
        self.__initialize_properties(movie)
        self.__initialize_cast(movie)
    
    def get_id(self):
        return self.id

    def __initialize_properties(self, movie) -> None:
        properties =['id',
        'short_description',
        'original_release_year',
        'object_type',
        'original_title']

        for property in properties:
            if property in movie:
                setattr(self, property, movie[property])
            else:
                setattr(self, property, "")
        

    def __initialize_cast(self, movie) -> None:
        self.cast = []
        if 'credits' not in movie:
            return
        for index, credit in enumerate(movie['credits']):
            self.cast.append(Cast(credit))
            if (index == 3):
                return

    def __group_cast(self) -> str:
        cast_str = ""
        for cast in self.cast:
            cast_str += str(cast) + "\n"

        return cast_str

    def __str__(self) -> str:
        return """
#{}

{} ({})

{}


{}
        """.format(
            self.id,
            self.original_title,
            self.original_release_year,
            self.short_description,            
            self.__group_cast(),
        )