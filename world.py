class Resource:
  def __init__(self, name, production, food):
    self.name = name
    self.production = production
    self.food = food
    self.score = food + production

  def __str__(self) -> str:
    return f"""
    Name: {self.name}\n
    Production: {self.production}\n
    Food: {self.food}\n
    Score: {self.score}
    """

  def get_summary(self):
    return list(self.name, self.production, self.food, self.score)

SOIL = Resource("Soil", 2, 5)
WATER = Resource("Fresh Water", 3, 2)
ANIMAL = Resource("Wild Animals", 2, 5)
WOOD = Resource("Wood", 3, 0)
STONE = Resource("Stone", 3, 0)
CORE = Resource("Common Ore", 5, 0)
SAND = Resource('Sand', 2, 0)
SPICE = Resource("Spice", 2, 3)
DYE = Resource("Dye", 2, 0)
RORE = Resource("Rare Ore", 5, 0)
GAME_RESOURCES = []
GAME_RESOURCES.append(SOIL)
GAME_RESOURCES.append(WATER)
GAME_RESOURCES.append(ANIMAL)
GAME_RESOURCES.append(WOOD)
GAME_RESOURCES.append(STONE)
GAME_RESOURCES.append(CORE)
GAME_RESOURCES.append(SAND)
GAME_RESOURCES.append(SPICE)
GAME_RESOURCES.append(DYE)
GAME_RESOURCES.append(RORE)

class Building:
  def __init__(self, name, food, production, buy_cost, sell_value, operation_cost, city, count):
    self.name = name
    self.food = food
    self.production = production
    self.buy_cost = buy_cost
    self.sell_value = sell_value
    self.operation_cost = operation_cost
    self.city = city
    #used to store how many of this building are in a city
    self.count = count
  
class Strategy_Building(Building):
  ### BASE -> turns into (convert_resource) at the rate of (conversion_rate)% of the amount of base resources that city posseses 
  def __init__(self, name, food, production, buy_cost, sell_value, operation_cost, city, count, base_resource, conversion_rate, convert_resource ):
    super().__init__(self, name, food, production, buy_cost, sell_value, operation_cost, city, count)   
    self.base_resource = base_resource
    self.conversion_rate = conversion_rate
    self.convert_resource = convert_resource
    self.home = city
    
    self.yields = 0

    base_yields = self.home.resources.get(base_resource)
    self.yields = base_yields * self.conversion_rate



class Luxary_Building(Building):
  def __init__(self, name, food, production, buy_cost, sell_value, operation_cost, city, count, score_bonus, influence_bonus, multiplier_bonus ):
    super().__init__(self, name, food, production, buy_cost, sell_value, operation_cost, city, count)   
    self.score = score_bonus
    self.influence = influence_bonus
    self.multiplier = multiplier_bonus


#RECIPES CAN BE UNITS OR STRATEGEMS
#CAPACITY IS ONLY FOR UNITS
class Military_Building(Building):
  def __init__(self, name, production, buy_cost, sell_value, operation_cost, city, count, capacity, recipe_list):
    super().__init__(self, name, 0, production, buy_cost, sell_value, operation_cost, city, count)   
    self.capacity = capacity
    self.recipes = []
    self.garrison = []
    for recipe in recipe_list:
      self.recipes.append(recipe)

  def garrison_unit(self, unit):
    if len(self.garrison) < self.capacity:
      self.garrison.append(unit)
    else:
      pass
      print("GARRISON FULL")

class Region:
  def __init__(self, name, soil, water, animal, wood, stone, core, sand, spice, dye, rore):
    self.name = name

    SOIL = Resource("Soil", 2, 5)
    WATER = Resource("Fresh Water", 3, 2)
    ANIMAL = Resource("Wild Animals", 2, 5)
    WOOD = Resource("Wood", 3, 0)
    STONE = Resource("Stone", 3, 0)
    CORE = Resource("Common Ore", 5, 0)
    SAND = Resource('Sand', 2, 0)
    SPICE = Resource("Spice", 2, 3)
    DYE = Resource("Dye", 2, 0)
    RORE = Resource("Rare Ore", 5, 0)
    self.GAME_RESOURCES = []
    self.GAME_RESOURCES.append(SOIL)
    self.GAME_RESOURCES.append(WATER)
    self.GAME_RESOURCES.append(ANIMAL)
    self.GAME_RESOURCES.append(WOOD)
    self.GAME_RESOURCES.append(STONE)
    self.GAME_RESOURCES.append(CORE)
    self.GAME_RESOURCES.append(SAND)
    self.GAME_RESOURCES.append(SPICE)
    self.GAME_RESOURCES.append(DYE)
    self.GAME_RESOURCES.append(RORE)
    
    self.resources = {}
    self.base_resources = {}

    self.resources.update({"Soil": soil})
    self.resources.update({"Fresh Water": water})
    self.resources.update({"Wild Animals": animal})
    self.resources.update({"Wood": wood})
    self.resources.update({"Stone": stone})
    self.resources.update({"Common Ore": core})
    self.resources.update({"Sand": sand})
    self.resources.update({"Spices": spice})
    self.resources.update({"Dye": dye})
    self.resources.update({"Rare Ore": rore})

    self.base_resources.update({"Soil": soil})
    self.base_resources.update({"Fresh Water": water})
    self.base_resources.update({"Wild Animals": animal})
    self.base_resources.update({"Wood": wood})
    self.base_resources.update({"Stone": stone})
    self.base_resources.update({"Common Ore": core})



  def get_available(self):
    available = {}
    for key, val in self.resources.items():
      if val >= 1:
        available.update({key : val})
    return available

  def get_available_base(self):
    available = {}
    for key, val in self.base_resources.items():
      if val >= 1:
        available.update({key : val})
    return available


class Island:
  def __init__(self, name, regions):
    self.name = name
    self.regions = regions

class WORLD:
  def __init__(self, name, islands):
    self.name = name
    self.islands = islands
    self.empires = []
    self.cities = []
    self.units = []
