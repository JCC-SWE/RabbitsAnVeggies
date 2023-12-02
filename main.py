from GameEngine import GameEngine

def main():
    # Instantiate a GameEngine object
    game_engine = GameEngine()

    # Initialize the game
    game_engine.initializeGame()

    # Display game introduction
    game_engine.intro()

    # Initialize the number of remaining vegetables
    remaining_veggies = game_engine.remainingVeggies()

    # Game loop
    while remaining_veggies > 0:
        # Print the field
        game_engine.printField()

        # Move the rabbits
        game_engine.moveRabbits()

        # Move the captain
        game_engine.moveCaptain()

        # Determine the new number of remaining vegetables
        remaining_veggies = game_engine.remainingVeggies()

    # Display Game Over information
    game_engine.gameOver()

    # Handle High Score functionality
    game_engine.highScore()

if __name__ == "__main__":
    main()
    
    
    
#  VeggieFile1.csv
