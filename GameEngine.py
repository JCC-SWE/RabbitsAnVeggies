import pickle
import random
import os
import random
from Rabbit import Rabbit
from Veggie import Veggie
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
        """
        Initializes field with vegetables based on input file.

        Prompts user to enter a file name and reads data from it.

        :return: None. Initializes the field with vegetables.
        """
        veggie_file_name = input("Please enter the name of the vegetable point file: ")

        # Validate existence of input file
        while not os.path.exists(veggie_file_name):
            veggie_file_name = input(f"{veggie_file_name} does not exist! Please enter the name of the vegetable point file: ")

        # Open and read the veggie file
        with open(veggie_file_name, 'r') as file:
            lines = file.readlines()

        # Initialize field with the size specified in the first line
        field_size = tuple(map(int, lines[0].strip().split(',')[1:]))
        self.field = [[None for _ in range(field_size[1])] for _ in range(field_size[0])]

        # Process remaining lines to create Veggie objects
        for line in lines[1:]:
            parts = line.strip().split(',')
            veggie = Veggie(parts[0], parts[1], int(parts[2]))
            self.vegetables.append(veggie)

        # Populate field with vegetables
        for _ in range(self.__NUMBEROFVEGGIES):
            while True:
                x, y = random.randint(0, field_size[0] - 1), random.randint(0, field_size[1] - 1)
                if self.field[x][y] is None:
                    self.field[x][y] = random.choice(self.vegetables)
                    break


    def initCaptain(self):
        while True:
            x, y = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)
            if self.field[x][y] is None:
                self.captain = Captain('V', x, y, [])
                self.field[x][y] = self.captain
                break

    def initRabbits(self):
        """
        Initializes field with a predefined number of rabbits

        For each rabbit, finds a random, unoccupied location on the field and 
        places a new rabbit object there.

        :return: None. Populates the field with rabbit objects without returning any value.
        """
        # Loop for number of rabbits
        for _ in range(self.__NUMBEROFRABBITS):
            # try until rabbit is placed
            while True:
                x, y = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)
                if self.field[x][y] is None:
                    # Create new rabbit
                    rabbit = Rabbit('R', x, y)
                    self.rabbits.append(rabbit)
                    # Place rabbit on field
                    self.field[x][y] = rabbit
                    break

    def initializeGame(self):
        """
        Initializes game environment by populating it with vegetables, captain, rabbits.

        Calls three methods: `initVeggies` to populate the field with vegetables, 
        `initCaptain` to place the captain, and `initRabbits` to distribute rabbits on the field. 

        :return: None. Just initializes the game state..
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
    

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
