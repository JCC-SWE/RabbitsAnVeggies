import pickle
import random
import os
import random
from Rabbit import Rabbit
from Snake import Snake
from Veggie import Veggie
from Captain import Captain


class GameEngine:
    __NUMBEROFVEGGIES = 30
    __NUMBEROFRABBITS = 5
    __HIGHSCOREPROFILE = "highscore.data"

    def __init__(self):

        """
        The __init__ function is called when the class is instantiated.
        It sets up the initial state of the object, and takes no arguments.

        :param self: Refer to the object itself
        :return: The object it creates
        :doc-author: Josh
        """
        self.field = []
        self.rabbits = []
        self.captain = None
        self.vegetables = []
        self.score = 0
        self.snake = None

    def initSnake(self):
        """
        Randomly places the snake in an unoccupied position on the field.
        
        :return: None. Initializes snake's position in the game field.
        :doc-author: Vatsal
        """
        while True:
            x, y = random.randint(0, len(self.field) - 1), random.randint(0, len(self.field[0]) - 1)
            if self.field[x][y] is None:
                self.snake = Snake(x, y)
                self.field[x][y] = self.snake
                break
    
            
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

        """
        The initCaptain function initializes the captain object.
            It does this by randomly generating a location for the captain on the field, and then placing him there.
            The while loop ensures that it will keep trying to find an empty spot until it finds one.

        :param self: Access the instance of the class
        :return: The captain object
        :doc-author: Josh
        """
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
        `initCaptain` to place the captain, and `initRabbits` to distribute rabbits on the field, `initSnake` to add snake in the field. 

        :return: None. Just initializes the game state..
        """
        self.initVeggies()
        self.initCaptain()
        self.initRabbits()
        self.initSnake()

    def remainingVeggies(self):   
        """
        The remainingVeggies function returns the number of veggies remaining in the field.
        It does this by iterating through each row and cell in self.field, checking if it is an instance of Veggie, and adding 1 to count for every instance found.

        :param self: Refer to the object itself
        :return: The number of veggies that are still on the field
        :doc-author: Josh
        """
        count = 0
        for row in self.field:
            for cell in row:
                if isinstance(cell, Veggie):
                    count += 1
        return count

    def intro(self):
        print("Welcome to Captain Veggie!")
        print("The rabbits have invaded your garden and you must harvest as many vegetables as possible before the rabbits eat them all! Each vegetable is worth a different number of points so go for the high score!")
        print("\nThe vegetables are:")
        for veg in self.vegetables:
            print(f"{veg.getWho()}: {veg.getName()} {veg.getPoints()} Points")
        print("\nCaptain Veggie is V, and the rabbits are R's.")
        print("\nGood luck!")

    def printField(self):
        """
        The printField function prints the current state of the field.
        It displays a border around the field, and two spaces between each element in a row.
        The function also displays how many vegetables are remaining on the field, as well as
        the player's current score.

        :param self: Refer to the object itself
        :return: None
        :doc-author: Josh
        """
        remaining_veggies = self.remainingVeggies()
        print(f"{remaining_veggies} veggies remaining. Current score: {self.score}")

        # top border
        border = '#' * (3 * len(self.field[0]) + 2)
        print(border)

        for row in self.field:
            row_str = '#'
            for cell in row:
                if cell is None:
                    row_str += '   '  
                else:
                    row_str += ' ' + cell.getWho() + ' ' 
            row_str += '#'
            print(row_str)

        # bottom border
        print(border)

    def getScore(self):
        return self.score

    def moveRabbits(self):

        """
        The moveRabbits function moves the rabbits around the field.
        It takes no arguments and returns nothing. It uses a list of directions to randomly choose a direction for each rabbit to move in, then checks if that new position is within bounds and not occupied by another rabbit or veggie. If it is, it moves the rabbit there.

        :param self: Refer to the object itself
        :return: None
        :doc-author: Josh
        """
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

        """
        The moveCptVertical function moves the captain vertically.
            It takes in a movement parameter, which is an integer that represents how many spaces to move.
            If the new x coordinate is within bounds of the field, it will move there and print out what happened.
            Otherwise, it will print out that you can't go that way.

        :param self: Refer to the object itself
        :param movement: Determine how far the captain moves
        :return: Nothing
        :doc-author: Josh
        """
        newX = self.captain.getX() + movement
        currentY = self.captain.getY()
        l = len(self.field)
        if 0 <= newX < l:
            self._moveCaptainTo(newX, currentY)
        else:
            print("You can't move that way!")

    def moveCptHorizontal(self, movement):

        """
        The moveCptHorizontal function takes in a movement value and moves the captain
        horizontally by that amount. If the new position is out of bounds, it prints an error message.

        :param self: Access the instance of the class
        :param movement: Determine how far the captain will move
        :return: A new y-coordinate for the captain
        :doc-author: Josh
        """
        newY = self.captain.getY() + movement
        currentX = self.captain.getX()
        if 0 <= newY < len(self.field[0]):
            self._moveCaptainTo(currentX, newY)
        else:
            print("You can't move that way!")

    def moveCaptain(self):

        """
        The moveCaptain function allows the user to move the captain around on the board.
        The function takes in a string input from the user and then moves Captain accordingly.
        If an invalid option is entered, it will print out that it is not a valid option.

        :param self: Refer to the object that is calling the method
        :return: Nothing
        :doc-author: Josh
        """
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
        """
        The gameOver function prints out the game over message, and then prints out
        the list of vegetables that the player managed to harvest. It also displays
        the score that the player achieved.

        :param self: Access the attributes of the class
        :return: A string
        :doc-author: Josh
        """
        print("GAME OVER!")
        print("You managed to harvest the following vegetables:")
        for veg in self.captain.getVeggieList():
            print(veg.getName())
        
        print(f"Your score was: {self.score}")

    def highScore(self):
        """
        The highScore function is called when the player loses. It asks for their initials and saves them to a file along with their score.
        It then displays all of the high scores in order from highest to lowest.

        :param self: Refer to the object itself
        :return: The high scores of the game
        :doc-author: Josh
        """
        try:
            with open(self.__HIGHSCOREPROFILE, 'rb') as file:
                highScores = pickle.load(file)
        except (FileNotFoundError, EOFError):
            highScores = []

        # Get player's initials
        initials = input("Please enter your three initials to go on the scoreboard: ")[:3]

        # Update high scores
        highScores.append((initials, self.score))
        highScores.sort(key=lambda x: x[1], reverse=True)

        # Display high scores
        print("HIGH SCORES")
        print("Name\tScore")
        for name, score in highScores:
            print(f"{name}\t{score}")

        # Save updated high scores
        with open(self.__HIGHSCOREPROFILE, 'wb') as file:
            pickle.dump(highScores, file)
        
    def _moveCaptainTo(self, newX, newY):
         # If the Rabbit had the position occupied
        """
        The _moveCaptainTo function is a helper function that moves the captain to a new position.
        It checks if there is an object in the new position and acts accordingly. If it's a rabbit,
        it prints out "Don't step on the bunnies" and returns without moving. If it's a veggie,
        it adds points to score and adds veggie to inventory.

        :param self: Refer to the object itself
        :param new_x: Set the new x position of the captain
        :param new_y: Set the y position of the captain
        :return: None
        :doc-author: Josh
        """
        if isinstance(self.field[newX][newY], Rabbit):
            print("Don't step on the bunnies!")
            return
        
        # If the Veggie had a position occupied
        if isinstance(self.field[newX][newY], Veggie):
            veggie = self.field[newX][newY]
            print(f"Yummy! A delicious {veggie.getName()}!")
            self.captain.addVeggie(veggie)  
            self.score += veggie.getPoints()

        self.field[self.captain.getX()][self.captain.getY()] = None 
        self.captain.setX(newX)  
        self.captain.setY(newY)  
        self.field[newX][newY] = self.captain

    def moveSnake(self):
        """
        Moves the snake towards the captain by calculating the shortest path
        
        :return: None. Updates snake's position on the field
        :doc-author: Vatsal
        """
        if self.snake is None:
            return

        snakeX, snakeY = self.snake.getX(), self.snake.getY()
        captainX, captainY = self.captain.getX(), self.captain.getY()

        # choosing direction for the snake to move closer to the captain
        xToMove = captainX - snakeX
        yToMove = captainY - snakeY
        moveX = 1 if xToMove > 0 else (-1 if xToMove < 0 else 0)
        moveY = 1 if yToMove > 0 else (-1 if yToMove < 0 else 0)

        newX = snakeX + moveX if abs(xToMove) > abs(yToMove) else snakeX
        newY = snakeY + moveY if abs(yToMove) > abs(xToMove) else snakeY

        # Check if the new position is valid, snake should be in the feild and not go out 
        if 0 <= newX < len(self.field) and 0 <= newY < len(self.field[0]):
            if self.field[newX][newY] is None:
                # Move the snake
                self.field[snakeX][snakeY] = None
                self.snake.setX(newX)
                self.snake.setY(newY)
                self.field[newX][newY] = self.snake
            elif self.field[newX][newY] is self.captain:
                self.handleSnakeEncounter()

    def handleSnakeEncounter(self):  
        """
        Handles the encounter between the snake and the captain
        
        :return: None. Modifies score and resets snake's position
        :doc-author: Vatsal
        """      
        for _ in range(5):
            if self.captain.getVeggieList():
                lastVeggie = self.captain.getVeggieList().pop()
                self.score -= lastVeggie.getPoints()
                if self.score < 0:
                    self.score = 0            

        # Reset the snake tosome random new position
        self.field[self.snake.getX()][self.snake.getY()] = None
        self.initSnake()
