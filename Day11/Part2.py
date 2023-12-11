# ADVENT OF CODE 2023
# --- Day 11: Cosmic Expansion ---
# https://adventofcode.com/2023/day/11#part2
# --- Part Two ---
#
# We used another method to solve this problem because we have
# to insert 1000000 lines per row/column with no galaxies.
# The method used in Part1.py is not efficient enough.
#
import re


def nums(s):
    m = re.findall("-?\d+", s)
    return [int(x) for x in m]


# Read the input file
with open("input.txt") as f:
    data = f.read().strip()

data = data.strip().split("\n")

# Find the position of galaxies and assign a number to each galaxy
# The number of galaxies is the number of "#" in the input file
# Find the position of row with no galaxies
# Find the position of column with no galaxies
galaxy_row = []
galaxy_col = []
num = 1
map_num = []
for i, lines in enumerate(data):
    for j, char in enumerate(lines):
        if data[i][j] == "#":
            galaxy_row.append(i)
            galaxy_col.append(j)
            map_num.append([i, j, num])
            num += 1

no_galaxies_row = [x for x in range(len(data)) if x not in galaxy_row]
no_galaxies_col = [x for x in range(len(data[0])) if x not in galaxy_col]

# Calculate the Manhattan distance between each pair of galaxies
# The Manhattan distance between two points (x1, y1) and (x2, y2) is
# |x1 - x2| + |y1 - y2|
# We count the number of row/column with no galaxies between two galaxies
# and add the Manhattan distance between them to the answer
# We can adjust the number of row/column with no galaxies between two galaxies
# by changing the constant 999999
ans = 0
i = 0
while i < len(map_num):
    j = i + 1
    while j < len(map_num):
        lower_bound_row, upper_bound_row = min(map_num[i][0], map_num[j][0]), max(
            map_num[i][0], map_num[j][0]
        )
        lower_bound_col, upper_bound_col = min(map_num[i][1], map_num[j][1]), max(
            map_num[i][1], map_num[j][1]
        )
        count_row = sum(
            lower_bound_row <= row <= upper_bound_row for row in no_galaxies_row
        )
        count_col = sum(
            lower_bound_col <= col <= upper_bound_col for col in no_galaxies_col
        )
        total = count_row + count_col
        distance = abs(map_num[i][0] - map_num[j][0]) + abs(
            map_num[i][1] - map_num[j][1]
        )
        ans += distance + total * 999999
        j += 1
    i += 1

print(ans)
