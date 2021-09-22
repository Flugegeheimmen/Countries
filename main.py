from country import *
from datetime import date

countries = CountryContainer()


countries.load_from_file('test.cts')

print(countries)
print(countries.search('rus'))
print(countries.remove(0))
print(countries)
print(countries.search('aus'))
