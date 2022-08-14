
from just_watch_crawler.country_fetch.JustWatchCountries import JustWatchCountries
from just_watch_crawler.providers.Netflix import Netflix
from justwatch import JustWatch
import time
import random
import pycountry
import flag


class CountryFetch:
    MIN_TIMEOUT = 1
    MAX_TIMEOUT = 2
    def __init__(self) -> None:
        self.providers = [
            Netflix()
        ]

    def cooldown(self):
        seconds = random.randint(self.MIN_TIMEOUT, self.MAX_TIMEOUT)

        print("waiting {} seconds...".format(seconds))
        time.sleep(seconds)

    def __get_list_of_providers_from_movies(self, movie):
        if 'offers' not in movie:
            return "(empty)"
    
        providers = []
        for offer in movie['offers']:
            movie_provider = offer['package_short_name']
            if (movie_provider not in providers):
                providers.append(movie_provider)
        
        str_providers = ", ".join(providers)
        return "({})".format(str_providers)

    def __get_list_of_providers(self):
        providers = []

        for provider in self.providers:
            providers.append(provider.get_code())
        return providers

    def search_by_providers(self, movie) -> bool:
        if 'offers' not in movie:
            return False

        for offer in movie['offers']:
            if (offer['package_short_name']) in self.__get_list_of_providers():
                return True
        return False 
        
    def country_feedback(self, country) -> None:
        country_flag = flag.flag(country)
        try:
            obj_country = pycountry.countries.get(alpha_2=country)
            return "{}  {}-{}".format(country_flag, country, obj_country.name)
        except:
            return "{} {}-{}".format('  ', country, country)

    def get_countries_by(self, movie_id: int):
        countries = JustWatchCountries().get_available_countries()
        time = int((len(countries) * self.MAX_TIMEOUT)/60)
        print("The search will take {} min...".format(time))

        countries_available = []
        for index, country in enumerate(countries):
            country = country.upper()
        
            try:
                just_watch = JustWatch(country=country)
                country_feeedback = self.country_feedback(country)
                print(country_feeedback + " - {}/{}".format(index + 1,len(countries)))

                movie = just_watch.get_title(title_id=movie_id, content_type='movie')

                providers = self.__get_list_of_providers_from_movies(movie)
                feedback = ""
                if (self.search_by_providers(movie)):
                    countries_available.append(country_feeedback)
                    feedback = "✅"
                print(movie['title']+ " " + feedback + " " + providers)
            except:
                print("ERROR")
            self.cooldown()
            
        return countries_available