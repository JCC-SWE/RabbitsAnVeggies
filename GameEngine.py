class GameEngine:
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREPROFILE = "highscore.data"

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
        # TODO: Initialize Captain
        pass

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
        # TODO: Get current score
        pass

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
