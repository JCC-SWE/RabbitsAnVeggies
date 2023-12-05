# Import the Creature class from the Creature module
# Author: Josh Cubero, Aman Patel, Vatsal Patel
# Date: 5/12/2023
# Description: This file creates the Captain class. Once instantiated, the captain is the first-person in the game.
from Creature import Creature


# Create a class named Captain that inherits from Creature
class Captain(Creature):

    # Constructor method for Captain class
    def __init__(self, x, y, vegList):
        # Call the constructor of the parent class (Creature)
        super().__init__("V", x, y)
        # Initialize the __vegList instance variable with the provided list
        self.__vegList = vegList

    # Method to add a vegetable to the __vegList
    def addVeggie(self, veg):
        self.__vegList.append(veg)
        
    def getVeggieList(self):
        return self.__vegList



