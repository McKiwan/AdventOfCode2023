# ADVENT OF CODE 2023
# --- Day 2: Cube Conundrum ---
# https://adventofcode.com/2023/day/2
# --- Part One ---
import pandas as pd

DATA_PATH = "input.txt"
# Set the maximum number of cubes for each color
MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14

# Read the input file
df = pd.read_csv(DATA_PATH, sep=":", header=None, names=["Game", "Cubes"])

# Get the game and cubes data in 2 different lists
game = df["Game"].tolist()
data = df["Cubes"].tolist()

# Loop through the games and cubes data to check which games IDs are valid
total = 0
for index, game in enumerate(data):
    # Split the cubes data into a list of different sets of cubes
    game_data = game.split(";")
    game_valid = True
    # Loop through the sets of cubes
    for item in game_data:
        # If the game is invalid, break out of the loop to go to the next game (2/2)
        if game_valid is False:
            break
        # Split the set of cubes into a list of different colors
        colors = item.split(",")
        for color in colors:
            # Check if the number of cubes for each color is greater than the maximum allowed number of cubes
            # If it is, the game is invalid, so break out of the loop to go to the next game (1/2)
            if "blue" in color:
                if int(color.split()[0]) > MAX_BLUE_CUBES:
                    game_valid = False
                    break
            elif "red" in color:
                if int(color.split()[0]) > MAX_RED_CUBES:
                    game_valid = False
                    break
            elif "green" in color:
                if int(color.split()[0]) > MAX_GREEN_CUBES:
                    game_valid = False
                    break
    # If the game is valid, print it and add its ID to the total
    if game_valid:
        print(f"Game {index + 1} is valid")
        total += index + 1
    # If the game is invalid, print it
    else:
        print(f"Game {index + 1} is invalid")

print(total)
