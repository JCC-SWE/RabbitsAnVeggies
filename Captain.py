# Import the Creature class from the Creature module
from Creature import Creature


# Create a class named Captain that inherits from Creature
class Captain(Creature):

    # Constructor method for Captain class
    def __init__(self, who, x, y, vegList):
        # Call the constructor of the parent class (Creature)
        super().__init__(who, x, y)
        # Initialize the __vegList instance variable with the provided list
        self.__vegList = vegList

    # Method to add a vegetable to the __vegList
    def addVeggie(self, veg):
        self.__vegList.append(veg)
        
    def getVeggieList(self):
        return self.__vegList



