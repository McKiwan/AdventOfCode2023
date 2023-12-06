# ADVENT OF CODE 2023
# --- Day 4: Scratchcards ---
# https://adventofcode.com/2023/day/4
# --- Part One ---
# Read the input file
with open("input.txt") as f:
    data = f.read().strip()
    f.close()

# Split the data into a list of lists to end up with a 2D list, one for winning numbers and one for numbers we have
data = data.split("\n")
data = [data[i].strip().split(":") for i in range(len(data))]
data = [data[i][1].strip() for i in range(len(data))]
data = [data[i].strip().split("|") for i in range(len(data))]
data = [
    [data[i][0].strip().split(), data[i][1].strip().split()] for i in range(len(data))
]

# Iterate through the data and find the numbers we have that are winning numbers
total = 0
for s in data:
    points = 0
    first_win = True
    for win_num in s[0]:
        if win_num in s[1]:
            if first_win:
                points += 1
                first_win = False
            else:
                points *= 2
    total += points

# Print the total which correspond to this rule :
# "The first match makes the card worth one point and each match after the first doubles the point value of that card."
print(total)
