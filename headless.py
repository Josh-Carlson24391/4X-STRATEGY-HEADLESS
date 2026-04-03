import time
import random
import os
from world import *
from city import City
from empire import Empire
from world import GAME_RESOURCES

class terminal:
    def __init__(self):
        self.world = None
        self.num_players = 0
        self.players = []


    #TODO!! AUTOGEN OPTION IS NON FUNCTION RIGHT NOW
    def world_setup(self):
        quit, status = False, False
        choice = int(input("-"*20 + "\nWORLD SETUP\n1. Manual\n2. Autogen\n3. Quit\n" + "-"*20 + "\n\n> "))
        if choice == 1:
            #ENTER MANUAL MODE
            os.system("clear")
            num_islands = int(input("-"*20 + "\nMANUAL WORLD CREATION\nPLEASE INPUT THE NUMBER OF ISLANDS\n" + "-"*20 + "\n\n> "))
            island_list = []
            
            os.system("clear")
            for island in range(num_islands):
                region_list = []
                num_regions = int(input("-"*20 + "\nMANUAL WORLD CREATION\nPLEASE INPUT THE NUMBER OF REGIONS FOR THE NEXT ISLAND\n" + "-"*20 + "\n\n> "))
                for region in range(num_regions):
                    name = str(input("-"*20  + "\nENTER REGION NAME\n" + "-"*20 + "\n\n >"))
                    
                    resources = {}
                    for resource in GAME_RESOURCES:
                        val = int(input(("-"*20  + f"\nHOW MUCH {resource.name} IS FOUND HERE?\n" + "-"*20 + "\n\n >")))
                        resources.update({resource.name : val})
                    os.system("clear")
                    region_list.append(Region(name, resources))

                name = str(input("-"*20  + "\nCURRENT ISLAND COMPLETED\nENTER ISLAND NAME\n" + "-"*20 + "\n\n >"))
                island_list.append(Island(name, region_list))
            #END OF WORLD CREATION
            name = str(input("-"*20  + "\nWORLD SETUP COMPLETE\nENTER WORLD NAME\n" + "-"*20 + "\n\n >"))
            self.world = WORLD(name, island_list)
            status = True
            
        elif choice == 2:
            #ENTER AUTOGEN MODE
            pass
        elif choice == 3:
            quit = True
            status = True

        return quit, status
    def Main(self):
        #MAIN LOOP
        QUIT = False
        WORLD_SETUP = False
        while(not QUIT):
            os.system("clear")
            #LAYER 0 - WORLD SETUP
            if WORLD_SETUP == False:
                while(WORLD_SETUP == False):
                    QUIT, WORLD_SETUP = self.world_setup()
            else:
                #LAYER 1 - GAME SETUP
                num_players = int(input("-"*20  + "\nGAME SETUP MENU\nENTER NUMBER OF PLAYERS\n" + "-"*20 + "\n\n >"))
                for player in range(num_players):
                    os.system("clear")
                    empire_name = input("-"*20  + f"\nPLAYER {player} ENTER EMPIRE NAME\n" + "-"*20 + "\n\n >")
                    os.system("clear")
                    print("ISLAND OPTIONS:")
                    for island in self.world.islands:
                        print(island.name)
                    starting_island = input("-"*20  + f"\nPLAYER {player} ENTER STARTING ISLAND\n" + "-"*20 + "\n\n >")
                    os.system("clear")
                    print("REGION OPTIONS:")
                    for island in self.world.islands:
                        if island.name == starting_island:
                            for region in island.regions:
                                print(region)
                    starting_region = input("-"*20  + f"\nPLAYER {player} ENTER STARTING REGION\n" + "-"*20 + "\n\n >")
                    os.system("clear")
                    capital_name = input("-"*20  + f"\nPLAYER {player} ENTER CAPITAL NAME\n" + "-"*20 + "\n\n >")
                    self.players.append(empire_name)
                    
                    #ADD CAPITAL TO WORLD
                    for island in self.world.islands:
                        if island.name == starting_island:
                            for region in island.regions:
                                if region.name == starting_region:
                                    city = City(capital_name, starting_island, starting_region, 1, empire_name)
                                    self.world.cities.append(city)
                                    region.cities.append(city)
                    
                print("END OF LAYER 1")

        os.system('clear')
        print("-"*20 + "\nThanks for Playing!\n" + 20*"-")

mainframe = terminal()
mainframe.Main()