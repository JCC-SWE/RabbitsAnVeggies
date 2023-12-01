import random

from Captain import Captain


class GameEngine:
    _NUMBEROFVEGGIES = 30
    _NUMBEROFRABBITS = 5
    HIGHSCOREPROFILE = "highscore.data"

    def __init__(self):
            self.field = []
            self.rabbits = []
            self.captain = None
            self.vegetables = []
            self.score = 0

    def initVeggies(self):
        # TODO: Initialize vegetables
        
        pass

    def initCaptain(self):
        while True:
            x, y = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)
            if self.field[x][y] is None:
                self.captain = Captain('V', x, y, [])
                self.field[x][y] = self.captain
                break

    def initRabbits(self):
        # TODO: Initialize rabbits
        pass

    def initializeGame(self):
        # TODO: Initialize the game
        pass

    def remainingVeggies(self):
        # TODO: Count remaining vegetables
        pass

    def intro(self):
        # TODO: Game introduction
        pass

    def printField(self):
        # TODO: Print the field
        pass

    def getScore(self):
        return self.score

    def moveRabbits(self):
        # TODO: Move rabbits
        pass

    def moveCptVertical(self, movement):
        # TODO: Move Captain vertically
        pass

    def moveCptHorizontal(self, movement):
        # TODO: Move Captain horizontally
        pass

    def moveCaptain(self):
        # TODO: Move Captain
        pass

    def gameOver(self):
        # TODO: Game over functionality
        pass

    def highScore(self):
        # TODO: High score functionality
        pass
