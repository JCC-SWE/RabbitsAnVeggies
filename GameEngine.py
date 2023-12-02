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
    

    def remainingVeggies(self):
        # return sum(1 for row in self.field for item in row if isinstance(item, Veggie))    
        count = 0
        for row in self.field:
            for cell in row:
                if isinstance(cell, Veggie):
                    count += 1
        return count

    def intro(self):
        print('''
    Welcome to Captain Veggie!
    The rabbits have invaded your garden and you must harvest
    as many vegetables as possible before the rabbits eat them
    all! Each vegetable is worth a different number of points
    so go for the high score!
        ''')
        print("The vegetables are:")
        for veg in self.vegetables:
            print(f"{veg.getWho()}: {veg.getName()} {veg.getPoints()} Points")
        print("\nCaptain Veggie is V, and the rabbits are R's.")
        print("\nGood luck!")

    def printField(self):
        # Display remaining vegetables and current score
        remaining_veggies = self.remainingVeggies()
        print(f"{remaining_veggies} veggies remaining. Current score: {self.score}")

        # top border
        border = '#' * (3 * len(self.field[0]) + 2)  # Adjust border length to account for extra spaces
        print(border)

        # Print field with border and two spaces between elements
        for row in self.field:
            row_str = '#'
            for cell in row:
                if cell is None:
                    row_str += '   '  # Three spaces for empty cell to align with two spaces after symbols
                else:
                    row_str += ' ' + cell.getWho() + ' '  # Symbol with two spaces after it
            row_str += '#'
            print(row_str)

        # bottom border
        print(border)

    def getScore(self):
        return self.score

    def moveRabbits(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (0, 0)]
        for rabbit in self.rabbits:
            dx, dy = random.choice(directions)
            new_x, new_y = rabbit.getX() + dx, rabbit.getY() + dy
            if 0 <= new_x < len(self.field) and 0 <= new_y < len(self.field[0]):
                # Check if new position is within bounds and not occupied by another rabbit
                if self.field[new_x][new_y] is None or isinstance(self.field[new_x][new_y], Veggie):
                    # Move rabbit to the new position and remove it from old position
                    self.field[rabbit.getX()][rabbit.getY()] = None
                    rabbit.setX(new_x)
                    rabbit.setY(new_y)
                    self.field[new_x][new_y] = rabbit

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

