# Author: Josh Cubero, Aman Patel, Vatsal Patel
# Date: 5/12/2023
# Description: This file creates the Snake class, which inherits from the Creature class. The snake is there to make the
# Captain's job more difficult.

from Creature import Creature


class Snake(Creature):
    def __init__(self, x, y):
        super().__init__('S', x, y)
