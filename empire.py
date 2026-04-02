import random
class Empire():
  def __init__(self, name, capital, current_year):
    self.name = name
    self.founded_in = current_year
    self.current_year = current_year
    self.capital = capital
    self.cities = []
    self.cities.append(self.capital)

    #!!!!!!!!! WORK IN PROGRESS ADDITIONS !!!!!!!!!
    self.roads = []
    
    self.basic_buildings = []
    self.strategy_buildings = []
    self.luxary_buildings = []
    self.military_buildings = []
    self.wonders = []
    self.all_buildings = []


  
    self.armies = []
    self.strategems = []

    #!!!!!!!! RETURN TO WORKING MODEL !!!!!!!!!!

    #EMPIRE ATTRIBUTES
    self.population = 0
    self.production = 0
    self.food = 0
    self.influence = 0
    self.taxes = 0
    self.city_count = 0

    self.science = 0
    self.culture = 0

    self.treasury = 0
    self.food_stock = 0
    self.research = 0
    self.alligence = 0

    self.resources = {}

    self.resources.update({"Soil": 0})
    self.resources.update({"Fresh Water": 0})
    self.resources.update({"Wild Animals": 0})
    self.resources.update({"Wood": 0})
    self.resources.update({"Stone": 0})
    self.resources.update({"Common Ore": 0})
    self.resources.update({"Sand": 0})
    self.resources.update({"Spices": 0})
    self.resources.update({"Dye": 0})
    self.resources.update({"Rare Ore": 0})


  def __str__(self):
    return f"""
    -------------------------------------
    {self.name}

    Cities: {self.city_count}
    -------------------------------------
    Resources: {self.get_resources_string()}
    -------------------------------------
    Empire Statistics:
    Population: {self.population}
    Production: {self.production} 
    Food: {self.food}
    Influence: {self.influence} 
    Taxes: ${self.taxes}
    -------------------------------------
    Culture: {self.culture}
    Science: {self.science}
    -------------------------------------
    Treasury: ${self.treasury}
    Food Stock: {self.food_stock}
    Alligence Points: {self.alligence}
    Research Points: {self.research}
    """

  def add_city(self, city):
    self.cities.append(city)

  def list_cities(self):
    print(f"""\n{self.name}""")
    for city in self.cities:  
      print(city)

  def get_cities(self):
    string = ""
    for city in self.cities: 
      string += str(city)
      string += "\n"
    return string

  def list_stats(self):
    print(self)

  

  def get_resources_string(self):
    string = f""
    for name, val in self.resources.items():
      string += f"\n{name}: {val}"
    return string

  def calc_stats(self):

    #RECALC CITY STATS
    for city in self.cities:
      city.calc_stats()

    #CALCULATE EMPIRE STATS FROM CITIES

    #CALC FOOD
    food = 0
    for city in self.cities:
      if not city.starved:
        food += city.food
    self.food = food

    #CALC PRODUCTION
    prod = 0
    for city in self.cities:
      if not city.starved:
        prod += city.production
    self.production = prod

    #CALC POPULATION
    pop = 0
    for city in self.cities:
      if not city.starved:
        pop += city.population
    self.population = pop

    #CALC Influence
    inf = 0
    for city in self.cities:
      if not city.starved:
        inf += city.influence
    self.influence = inf

    #CALC TAX
    tax = 0
    for city in self.cities:
      if not city.starved:
        tax += city.taxes
    self.taxes = tax

    #CALC Science + Culture

    #MUST HAVE INFLUENCE TO GAIN SCIENCE AND CULTURE
    if self.influence > 0:
      self.science = int((self.population * self.production) /  self.influence)
      self.culture = int((self.population * self.food) /  self.influence)

    #CALC NET GAINS
    self.research += self.science
    self.treasury += self.taxes
    self.alligence += self.culture
    self.food_stock += self.food 

    #CALC EMPIRE RESOURCES

    #Reset previous values
    for resource, value in self.resources.items():
      self.resources.update({resource : 0})

    #Get updated values from cities
    for city in self.cities:
      for k, v in self.resources.items():
        self.resources.update({k : (v + city.resources.get(k))})

    self.city_count = 0
    for city in self.cities:
      if not city.starved:
        self.city_count += 1
    for city in self.cities:
      city.empire = self.name
  def advance_time(self, years):
    for year in range(years):
      print(year)
      self.calc_stats()
    self.current_year = self.current_year + years
    return self.current_year
