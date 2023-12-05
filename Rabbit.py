# Import the Creature class from the Creature module
from Creature import Creature


# Create a class named Rabbit that inherits from Creature
class Rabbit(Creature):

    # Constructor method for Rabbit class
    def __init__(self, x, y):
        # Call the constructor of the parent class (Creature)
        super().__init__("R", x, y)


