
from just_watch_crawler.country_fetch.JustWatchCountries import JustWatchCountries
from just_watch_crawler.providers.DisneyPlus import DisneyPlus
from just_watch_crawler.providers.Globoplay import Globoplay
from just_watch_crawler.providers.Netflix import Netflix
from justwatch import JustWatch
import time
import pycountry
import flag
from progress.bar import IncrementalBar



class CountryFetch:
    MIN_TIMEOUT = 1
    MAX_TIMEOUT = 2
    def __init__(self) -> None:
        self.providers = [
            Netflix(),
            DisneyPlus(),
            Globoplay()
        ]

    def cooldown(self):
        time.sleep(0.125)

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
            return "{}  {}".format(country_flag, obj_country.name)
        except:
            return "{} {}".format('  ', country, country)

    def get_countries_by(self, movie_id: int):
        countries = JustWatchCountries().get_available_countries()

        bar = IncrementalBar('Searching...', max=len(countries), suffix='%(percent).2d%% %(elapsed_td)ss %(avg).3ss/country ')
        countries_available = []
        for country in countries:
            bar.next()
            try:
                just_watch = JustWatch(country=country.upper())
                country_feeedback = self.country_feedback(country.upper())
                movie = just_watch.get_title(title_id=movie_id, content_type='movie')

                providers = self.__get_list_of_providers_from_movies(movie)
                if (self.search_by_providers(movie)):
                    countries_available.append("{} {}".format(country_feeedback, providers))
                    print("{} - {} {}".format(country_feeedback, movie['title'], providers))
            except:
                pass
            self.cooldown()
        bar.finish()
            
        return countries_available