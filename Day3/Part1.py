# ADVENT OF CODE 2023
# --- Day 3: Gear Ratios ---
# https://adventofcode.com/2023/day/3
# --- Part One ---
import pandas as pd

DATA_PATH = "input.txt"

# Read the input file
df = pd.read_csv(DATA_PATH, header=None)
data = df[0].tolist()

# Get the max row and column
max_row = len(data)
max_col = len(data[0])


# Check if the number is valid, valid means it is adjacent to a symbol
def valid_number(data, number, row, col):
    col_start = col - len(number) - 1 if col - len(number) >= 0 else 0
    col_end = col
    row_start = row - 1 if row - 1 >= 0 else 0
    row_end = row + 1 if row + 1 < max_row else max_row - 1
    for i in range(row_start, row_end + 1):
        for j in range(col_start, col_end + 1):
            if not data[i][j].isdigit() and not data[i][j] == ".":
                return True


# Iterate through the data and find the numbers
total = 0
i = 0
while i in range(len(data)):
    j = 0
    while j in range(len(data[i])):
        number = ""
        if data[i][j].isdigit():
            while data[i][j].isdigit():
                number += data[i][j]
                if (j + 1) < max_col:
                    j += 1
                    continue
                break
            # We found a number, check if it is valid
            if valid_number(data, number, i, j):
                total += int(number)
        j += 1
    i += 1

# Print the total which is sum of all valid numbers
print(total)
