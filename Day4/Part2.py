# ADVENT OF CODE 2023
# --- Day 4: Scratchcards ---
# https://adventofcode.com/2023/day/4#part2
# --- Part Two ---
# Read the input file
with open("input.txt") as f:
    data = f.read().strip()
    f.close()

# Split the data into a list of lists to end up with a 2D list, one for winning numbers and one for numbers we have
data = data.split("\n")
data = [data[i].strip().split(":") for i in range(len(data))]
data = [data[i][1].strip() for i in range(len(data))]
data = [data[i].strip().split("|") for i in range(len(data))]
# Add a third element to the list to keep track of the number of times we have to count the card
data = [
    [data[i][0].strip().split(), data[i][1].strip().split(), 1]
    for i in range(len(data))
]

# Iterate through the data and find how manny winning numbers we have
total = 0
for index, s in enumerate(data):
    nb_win_card = 0
    first_win = True
    for win_num in s[0]:
        if win_num in s[1]:
            if first_win:
                nb_win_card += 1
    # If we have winning cards, we add one copy of the next 'x' cards
    # Where 'x' is the number of winning cards we have
    if nb_win_card > 0:
        for i in range(nb_win_card):
            data[index + i + 1][2] += 1 * s[2]

# Iterate through the data and find how many total scratchcards do you end up with
total = sum(s[2] for s in data)
print(total)
