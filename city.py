#CITY CLASS DEF

class City:
  def __init__(self, name, region, population, empire):
    self.starved = False
    self.name = name
    self.region = region
    self.empire = empire
   
   
   #TODO -> ADD GARRISON FUNCTIONALITY
    self.garrison_slots = 0
    self.total_unit_slots = 0
    self.occupying_force = []
   
   ### WORK IN PROGRESS ###
   
    self.roads = []
    
    self.basic_buildings = []
    self.strategy_buildings = []
    self.luxary_buildings = []
    self.military_buildings = []
    self.wonders = []
    self.all_buildings = []


  
    self.armies = []
    self.strategems = []
   
   ### END OF WORK IN PROGRESS ###

    #Each City starts with 4 slots for resources
    self.resource_slots = 4
    #Container for resource counts
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



    self.init_slots()

    self.population = population
    self.production = 0
    self.food = 0
    self.influence = 0
    self.taxes = 0

    self.score = 0
    self.multiplier = 0


    self.calc_stats()

    # print(f"Region of {self.region.name}")
    # for key, val in self.region.resources.items():
    #   print(f"{key}:{val}")

  def init_slots(self):
    in_region = self.region.get_available_base()
    for slot in range (self.resource_slots):
      #Select a random available resource
      source = random.choice(list(in_region.keys()))
      #Remove resource from regions pool
      self.region.resources.update({source : (self.region.resources.get(source) - 1)})
      #Add resource to city
      self.resources.update({source : (self.resources.get(source) + 1)})

  #GARRISON FUNCTIONALITY - TODO -> ADD UNIT FUNCTIONALITY
  def garrison_unit(self, unit):
    if len(self.garrison) < self.garrison_slots:
      unit.SET_HOME(str(self.name + "Garrison"))
      self.occupying_force.append(unit)
      return 0

    building_cap= 0
    for building in self.military_buildings:
      building_cap += building.capacity

    if building_cap > 0:
      unit.SET_HOME(str(self.name + "Military Building"))
      self.occupying_force.append(unit)

  def add_resource(self, target_name):
    in_region = self.region.get_available()
    #ONLY UPDATE IF SLOTS ARE AVAILABLE
    if self.get_open_resource_slots() > 0:
      for name, val in in_region.items():
        if name == target_name:
          #Remove resource from region pool
          self.region.resources.update({name : (self.region.resources.get(name) - 1)})
          #Add resource to city pool
          self.resources.update({name : (self.resources.get(name) + 1)})
          #print(f"ADDED {name} to {self.name}")
    else:
      print('ERROR NO SLOTS AVAILABLE')

  def get_open_resource_slots(self):
    slots = self.resource_slots
    for key, val in self.resources.items():

      if val >= 1:

        slots -= val
      if slots <= 0:
        return 0
    return slots

  def get_resource_summary(self):
    actual_sources = {}
    for key, val in self.resources.items():
      if val >= 1:
        #Add to list of actual resources
        actual_sources.update({key : val})
    return actual_sources

  def calc_stats(self):

    #TODO -> ADD  add-BUILDING FUNCTIONS for each type pf building

    #DONE -> CALC LIST OF BUILDINGS FROM CATEGORIES 
    all_buildings = []
    for building in self.basic_buildings:
      all_buildings.append(building)
    for building in self.strategy_buildings:
      all_buildings.append(building)
    for building in self.luxary_buildings:
      all_buildings.append(building)
    for building in self.military_buildings:
      all_buildings.append(building)
    self.all_buildings = all_buildings
    
    
    
    #CALC FOOD -- TODO -> 
    food = 0
    sources = self.get_resource_summary()
    for k, v in sources.items():
      for item in GAME_RESOURCES:
        if item.name == k:
          food += item.food * v

    #ADD FOOD FROM ALL BUILDINGS
    for building in self.all_buildings:
      food += building.food
    self.food = int(food)

    #CALC PRODUCTION - TODO -> ADD ALL BUILDINGS
    prod = 0
    sources = self.get_resource_summary()
    for k, v in sources.items():
      for item in GAME_RESOURCES:
        if item.name == k:
          prod += item.production

    #ADD FOOD FROM ALL BUILDINGS
    for building in self.all_buildings:
      prod += building.production
    self.production = int(prod)


    #CALC INFLUENCE, SCORE, and MULTIPLIER

    avg = 0
    i = 0
    for k, v in self.get_resource_summary().items():
      for item in GAME_RESOURCES:
        if item.name == k:
          avg += item.score
          i += 1
    avg = avg / i
    self.score = avg

    if self.food > 0 and self.population > 0:
      self.multiplier = self.food / self.population
    else:
      self.multiplier = 0

    self.influence = self.multiplier * self.score

    #CALC POPULATION CHANGE
    change = 0
    if self.food > 0:
      growth = (self.food / self.population)
    
      if self.food >= self.population:
        if self.influence > 0:
          change = (growth / self.influence)
      else:
        if self.population >= 0.5:
          change = -(self.population / 10)
    else:
      #CITY IS DESERTED IF IT DROPS BELOW 0.5 POPULATION
      if self.population < 0.5:
        self.population = 0
        self.starved = True
      else:
        change = -(self.population / 10)

    self.population += change


    #CALC INFLUENCE, SCORE, and MULTIPLIER after population change
    #TODO -> ADD LUXARY BUILDINGS
    avg = 0
    i = 0
    for k, v in self.get_resource_summary().items():
      for item in GAME_RESOURCES:
        if item.name == k:
          avg += item.score
          i += 1
    avg = avg / i
    
    self.score = avg
    for building in self.luxary_buildings:
      self.score += building.score

    if self.food > 0 and self.population > 0:
      self.multiplier = self.food / self.population
    else:
      self.multiplier = 0

    for building in self.luxary_buildings:
      self.multiplier += building.multiplier

    self.influence = self.multiplier * self.score
    
    for building in self.luxary_buildings:
      self.influence += building.influence

    #CALC TAXES
    self.taxes =int( self.influence * self.production * self.population)


    #CALC RESOURCES
    #ADD RESOURCES GAINED FROM STRATEGY BUILDINGS
    #WILL BE DONE WHEN YOU MODIFY THE NUMBER OF BUILDINGS






  def get_stat_summary(self):
    fetch = []
    fetch.append(self.population)
    fetch.append(self.production)
    fetch.append(self.food)
    fetch.append(self.influence)
    fetch.append(self.taxes)
    fetch.append(self.score)
    fetch.append(self.multiplier)
    return fetch

  def display_stats(self):
    stats = self.get_stat_summary
    print(f"""
    City of {self.name}:\n
    Population: {self.population}\n
    Production: {self.production} \n
    Food: {self.food}\n
    Influence: {self.influence} \n
    Taxes: {self.taxes}\n\n
    Resource Score: {self.score}\n
    Score Multiplier: {self.multiplier}\n
    """)

  def display_resources(self):
    print(f"City of {self.name}")
    for key, val in self.resources.items():
      print(f"{key}:{val}")


  def get_resources(self):
    source_list = {}
    for key, val in self.resources.items():
      source_list.update({key:val})
    return source_list

  def get_resources_string(self):
    string = f""""""
    for name, val in self.resources.items():
      string += f"\n{name}: {val}"
    return string

  def __str__(self):

    if self.population < 0.5:
      return f"""
      There lies nothing here but ruins...
      Population of {self.name} starved to death.
      """
    else:
        
      return f"""
      -------------------------------------
      City of {self.name}
      Resources: {self.get_resources_string()}
      City Statistics:\n
      Population: {self.population}
      Production: {self.production} 
      Food: {self.food}
      Influence: {self.influence} 
      Taxes: ${self.taxes}
      -------------------------------------
      Resource Score: {self.score}
      Score Multiplier: {self.multiplier}
      -------------------------------------
      """
