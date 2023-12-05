# Create a class named FieldInhabitant
# Author: Josh Cubero, Aman Patel, Vatsal Patel
# Date: 5/12/2023
# Description: This file creates the parent class for Creature and Captain.
class FieldInhabitant:
    # Constructor method for FieldInhabitant class
    def __init__(self, who):
        # Initialize a protected instance variable _who
        self._who = who

    # Setter method to set the value of _who
    def setWho(self, who):
        self._who = who

    # Getter method to get the value of _who
    def getWho(self):
        return self._who
