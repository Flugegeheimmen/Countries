from country import *
from datetime import date


countries = CountryContainer()

countries.add(Country('Russia', 'Moscow', date(1991, 12, 25), 17130000, 144400000))

print(countries)

print(countries.search('rus'))
