# ADVENT OF CODE 2023
# --- Day 3: Gear Ratios ---
# https://adventofcode.com/2023/day/3#part2
# --- Part Two ---
import pandas as pd

DATA_PATH = "input.txt"

# Read the input file
df = pd.read_csv(DATA_PATH, header=None)
data = df[0].tolist()
max_row = len(data)
max_col = len(data[0])


# Check if the number is valid, valid means it is adjacent to "*" symbol
def valid_number(array, data, number, row, col):
    col_start = col - len(number) - 1 if col - len(number) >= 0 else 0
    col_end = col
    row_start = row - 1 if row - 1 >= 0 else 0
    row_end = row + 1 if row + 1 < max_row else max_row - 1
    for i in range(row_start, row_end + 1):
        for j in range(col_start, col_end + 1):
            # If the number is adjacent to "*" symbol, add it to the array with its row and column
            if data[i][j] == "*":
                array.append([number, i, j])
                return True


# Iterate through the data and find the numbers
array = []
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
            valid_number(array, data, number, i, j)
        j += 1
    i += 1

# Find numbers that are adjacent to the same "*" symbol and multiply them
total = 0
i = 0
while i in range(len(array)):
    j = i + 1
    while j in range(j, len(array)):
        if (array[i][1]) == array[j][1] and (array[i][2]) == array[j][2]:
            print(
                f"{array[i][0]} * {array[j][0]} = {int(array[i][0]) * int(array[j][0])}"
            )
            total += int(array[i][0]) * int(array[j][0])
        j += 1
    i += 1

# Print the total which is sum of all the multiplied numbers
print(total)
