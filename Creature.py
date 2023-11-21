# Import the FieldInhabitant class from the FieldInhabitant module
from FieldInhabitant import FieldInhabitant


# Create a class named Creature that inherits from FieldInhabitant
class Creature(FieldInhabitant):

    # Constructor method for Creature class
    def __init__(self, who, x, y):
        # Call the constructor of the parent class (FieldInhabitant)
        super().__init__(who)
        # Initialize private instance variables __x and __y
        self.__x = x
        self.__y = y

    # Getter method to get the x-coordinate of the creature
    def getX(self):
        return self.__x

    # Setter method to set the x-coordinate of the creature
    def setX(self, x):
        self.__x = x

    # Getter method to get the y-coordinate of the creature
    def getY(self):
        return self.__y

    # Setter method to set the y-coordinate of the creature
    def setY(self, y):
        self.__y = y


creature = Creature('c', 5, 9)
print(creature.getX())
print(creature.getY())


