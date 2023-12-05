# ADVENT OF CODE 2023
# --- Day 2: Cube Conundrum ---
# https://adventofcode.com/2023/day/2#part2
# --- Part Two ---
import pandas as pd

DATA_PATH = "input.txt"

# Read the input file
df = pd.read_csv(DATA_PATH, sep=":", header=None, names=["Game", "Cubes"])
game = df["Game"].tolist()
data = df["Cubes"].tolist()

# Loop through the games and cubes data
total = 0
for index, game in enumerate(data):
    # Split the cubes data into a list of different sets of cubes
    game_data = game.split(";")
    # Set the minimum number of cubes for each color to 0
    min_number_of_red_cubes = 0
    min_number_of_green_cubes = 0
    min_number_of_blue_cubes = 0
    # Loop through the sets of cubes
    for item in game_data:
        # Split the set of cubes into a list of different colors
        colors = item.split(",")
        # Loop through the colors
        for color in colors:
            # Check if the number of cubes for each color is greater than the minimum number of cubes
            # If it is, set the minimum number of cubes to that number
            if "blue" in color:
                if int(color.split()[0]) > min_number_of_blue_cubes:
                    min_number_of_blue_cubes = int(color.split()[0])
            elif "red" in color:
                if int(color.split()[0]) > min_number_of_red_cubes:
                    min_number_of_red_cubes = int(color.split()[0])
            elif "green" in color:
                if int(color.split()[0]) > min_number_of_green_cubes:
                    min_number_of_green_cubes = int(color.split()[0])
    # Print the minimum number of cubes for each color
    print(
        f"Game {index + 1}: {min_number_of_red_cubes} red cubes, {min_number_of_green_cubes} green cubes, {min_number_of_blue_cubes} blue cubes"
    )
    # Print the power of all this numbers
    print(
        f"Total number = {min_number_of_red_cubes * min_number_of_green_cubes * min_number_of_blue_cubes}"
    )
    # Add the power of all this numbers to the total
    total += (
        min_number_of_red_cubes * min_number_of_green_cubes * min_number_of_blue_cubes
    )

print(total)
