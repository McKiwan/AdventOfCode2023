# ADVENT OF CODE 2023
# --- Day 6: Wait For It ---
# https://adventofcode.com/2023/day/6
# --- Part One ---
# Read the input file
with open("input.txt") as f:
    data = f.read().strip()

# Split the data to put time and distance in 2 different lists
data = data.strip().split("\n")
data = [x.strip().split(":")[1:] for x in data]
for i, x in enumerate(data):
    data[i] = [y.strip().split() for y in x]
    data[i] = [int(y) for y in data[i][0]]
times = data[0]
distances = data[1]

# Calculate the number of differents ways to beat the record for each time
ans = 1
for i, time in enumerate(times):
    x = 0
    total = 0
    while x < time:
        timeleft = time - x
        if (x * timeleft) > distances[i]:
            total += 1
        x += 1
    print(
        f"There is {total} differents way to beat the record of {distances[i]} millimeters"
    )
    ans *= total

print(ans)
