
from just_watch_crawler.country_fetch.JustWatchCountries import JustWatchCountries
from justwatch import JustWatch
import time
import random
import pycountry
import flag


class CountryFetch:
    MIN_TIMEOUT = 2
    MAX_TIMEOUT = 4
    def __init__(self) -> None:
        pass

    def cooldown(self):
        seconds = random.randint(self.MIN_TIMEOUT, self.MAX_TIMEOUT)

        print("waiting {} seconds...".format(seconds))
        time.sleep(seconds)

    def search_by_providers(movie):
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

        for index, country in enumerate(countries):
            country = country.upper()
        
            try:
                just_watch = JustWatch(country=country)
                print(self.country_feedback(country) + " - {}/{}".format(index + 1,len(countries)))
                
                movie = just_watch.get_title(title_id=movie_id, content_type='movie')
            
                print(movie['title'])
            except:
                print("ERROR")
            self.cooldown()
        return