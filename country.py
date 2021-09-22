class Country:
    def __init__(self, name, capital, established, area, population):
        self.name = name
        self.capital = capital
        self.established = established
        self.area = area
        self.population = population

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class CountryContainer:
    countries = []

    def __init__(self):
        pass

    def search(self, key):
        search_date = []
        for id, country in enumerate(self.countries):
            if country and key.lower() in country.name.lower():
                search_date.append([id, country])
        return search_date

    def add(self, country):
        if country in self.countries:
            return False
        return self.countries.append(country)

    def remove(self, id):
        if 0 <= id < len(self.countries):
            self.countries[id] = None
            return True
        return False

    def update(self, id, country):
        if 0 <= id < len(self.countries):
            self.countries[id] = country
            return True
        return False

    def __repr__(self):
        return self.countries.__str__()
