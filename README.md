# just_watch_crawler

A project based into JustWatch features (https://www.justwatch.com/) using https://github.com/dawoudt/JustWatchAPI


# How to use?

Enter on poetry env
```
poetry shell
```

Install the dependencies
```
poetry install
````

and then run
```
python3 just_watch_crawler/main.py
```

# Limitations

Now the project just search for three providers (Netflix, Globoplay and Disney+). Please add more providers into *CountryFetch* constructor's `/just_watch_crawler/country_fetch/CountryFetch.py` 

Feel free to change the countries as well in JustWatchCountries `/just_watch_crawler/country_fetch/JustWatchCountries.py`. The country codes follows the `iso 3166` 