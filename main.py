import pickle
from GameEngine import GameEngine

def loadHighScores(filename):
    try:
        with open(filename, 'rb') as data:
            return pickle.load(data)
    except FileNotFoundError:
        return []

def saveHighScores(file, highScores):
    with open(file, 'wb') as data:
        pickle.dump(highScores, data)

def updateHighScores(highScores, user, score):
    highScores.append((user, score))
    highScores.sort(key=lambda x: x[1], reverse=True)  # Assuming the second element is the score
    return highScores

def printHighScores(highScores):
    print("High Scores:")
    for user, score in highScores:
        print(f"{user}: {score}")

def main():
    # Load high scores
    highScores = loadHighScores(GameEngine.__HIGHSCOREPROFILE)

    # Game initialization
    game = GameEngine()
    game.initializeGame()
    game.intro()

    # Main game loop
    while game.remainingVeggies() > 0:
        print(f"Remaining Vegetables: {game.remainingVeggies()}, Score: {game.getScore()}")
        game.printField()
        game.moveRabbits()
        game.moveCptVertical()  # Assuming this is the method to move the captain

    # Game Over
    print("Game Over!")

    # Handle High Scores
    user = input("Enter your initials: ")[:3].upper()
    score = game.getScore()
    highScores = updateHighScores(highScores, user, score)
    printHighScores(highScores)
    saveHighScores(GameEngine.HIGHSCOREPROFILE, highScores)

main()


