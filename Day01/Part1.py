# ADVENT OF CODE 2023
# --- Day 1: Trebuchet?! ---
# https://adventofcode.com/2023/day/1
# --- Part One ---
import pandas as pd

DATA_PATH = "input.txt"

# Read the input file
df = pd.read_csv(DATA_PATH, header=None)
data = df[0].tolist()

# Calculate the total sum of the first and last number in each line
total = 0
for word in data:
    value = 0
    for char in word:
        if char.isnumeric():
            value += int(char) * 10
            break
    for char in reversed(word):
        if char.isnumeric():
            value += int(char)
            break
    total += value

print(total)
