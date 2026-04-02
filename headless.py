import time
import random
from world import *
from city import City
from empire import Empire

region1 = Region("Ratana", 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
city1 = City("Al-Bazir", region1, 1, "Akhomus")
empire = Empire("YIYIA", city1, 200)
