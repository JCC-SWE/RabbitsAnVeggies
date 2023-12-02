import pickle
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
        movement = input("Would you like to move up(W), down(S), left(A), or right(D): ").strip().lower()
        if movement == 'w':
            self.moveCptVertical(-1)  
        elif movement == 's':
            self.moveCptVertical(1)  
        elif movement == 'a':
            self.moveCptHorizontal(-1) 
        elif movement == 'd':
            self.moveCptHorizontal(1) 
        else:
            print(f"{movement} is not a valid option")

    def gameOver(self):
        print("GAME OVER!")
        print("VYou managed to harvest the following vegetables:")
        for veg in self.captain.getVeggieList():
            print(veg.getName())
        
        print(f"Your score was: {self.score}")

    def highScore(self):
        # Load existing high scores
        try:
            with open(self.__HIGHSCOREPROFILE, 'rb') as file:
                high_scores = pickle.load(file)
        except (FileNotFoundError, EOFError):
            high_scores = []

        # Get player's initials
        initials = input("Please enter your three initials to go on the scoreboard: ")[:3]

        # Update high scores
        high_scores.append((initials, self.score))
        high_scores.sort(key=lambda x: x[1], reverse=True)

        # Display high scores
        print("HIGH SCORES")
        print("Name\tScore")
        for name, score in high_scores:
            print(f"{name}\t\t{score}")

        # Save updated high scores
        with open(self.__HIGHSCOREPROFILE, 'wb') as file:
            pickle.dump(high_scores, file)
