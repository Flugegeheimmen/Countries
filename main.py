from country import *
from datetime import date


countries = CountryContainer()

countries.add(Country('Russia', 'Moscow', date(1991, 12, 25), 17130000, 144400000))
countries.add(Country('Australia', 'Canberra', date(1901, 1, 1), 7692000, 25360000))

print(countries)
print(countries.search('rus'))
print(countries.remove(0))
print(countries)
print(countries.search('aus'))
