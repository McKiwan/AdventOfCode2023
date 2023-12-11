# ADVENT OF CODE 2023
# --- Day 11: Cosmic Expansion ---
# https://adventofcode.com/2023/day/11
# --- Part One ---
import re


def nums(s):
    m = re.findall("-?\d+", s)
    return [int(x) for x in m]


# Double the size of row and column with no galaxies
def insert_empty_line(data, no_galaxies_row, no_galaxies_col):
    transposed_data = ["".join(colonne) for colonne in zip(*data)]
    empty_line = "." * len(transposed_data[0])
    for i in reversed(no_galaxies_col):
        transposed_data.insert(i, empty_line)

    data = ["".join(colonne) for colonne in zip(*transposed_data)]
    empty_line = "." * len(data[0])
    for i in reversed(no_galaxies_row):
        data.insert(i, empty_line)
    return data


# Read the input file
with open("input.txt") as f:
    data = f.read().strip()


data = data.strip().split("\n")

# Find the position of row with no galaxies
# Find the position of column with no galaxies
galaxy_row = []
galaxy_col = []
for i, lines in enumerate(data):
    for j, char in enumerate(lines):
        if data[i][j] == "#":
            galaxy_row.append(i)
            galaxy_col.append(j)
no_galaxies_row = [i for i in range(len(data)) if i not in galaxy_row]
no_galaxies_col = [i for i in range(len(data[0])) if i not in galaxy_col]

# Double the size of row and column with no galaxies
data = insert_empty_line(data, no_galaxies_row, no_galaxies_col)

# Find the position of galaxies and assign a number to each galaxy
# The number of galaxies is the number of "#" in the input file
num = 1
map_num = []
for i, lines in enumerate(data):
    for j, char in enumerate(lines):
        if data[i][j] == "#":
            map_num.append([i, j, num])
            num += 1

# Calculate the Manhattan distance between each pair of galaxies
ans = 0
i = 0
while i < len(map_num):
    j = i + 1
    while j < len(map_num):
        distance = abs(map_num[i][0] - map_num[j][0]) + abs(
            map_num[i][1] - map_num[j][1]
        )
        ans += distance
        j += 1
    i += 1

print(ans)
