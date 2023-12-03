# Import the FieldInhabitant class from the FieldInhabitant module
from FieldInhabitant import FieldInhabitant


# Create a class named Veggie that inherits from FieldInhabitant
class Veggie(FieldInhabitant):

    # Constructor method for Veggie class
    def __init__(self, name, who, points):
        # Call the constructor of the parent class (FieldInhabitant)
        super().__init__(who)
        # Initialize private instance variables __name and __points
        self.__name = name
        self.__points = points

    # Setter method to set the name of the veggie
    def setName(self, name):
        self.__name = name

    # Getter method to get the name of the veggie
    def getName(self):
        return self.__name

    # Setter method to set the points of the veggie
    def setPoints(self, points):
        self.__points = points

    # Getter method to get the points of the veggie
    def getPoints(self):
        return self.__points

    # Override the __str__ method to provide a string representation of the Veggie object
    def __str__(self):
        return f'Name: {self.__name}\nSymbol: {self._who}\nPoints: {self.__points}'



    

