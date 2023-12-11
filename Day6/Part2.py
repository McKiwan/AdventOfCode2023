# ADVENT OF CODE 2023
# --- Day 6: Wait For It ---
# https://adventofcode.com/2023/day/6#part2
# --- Part Two ---
# Read the input file
with open("input.txt") as f:
    data = f.read().strip()

# Split the data to remove text and put time and distance in 2 different variables
data = data.strip().split("\n")
data = [x.strip().split(":")[1:] for x in data]
for i, x in enumerate(data):
    data[i] = [y.strip().split() for y in x]
    data[i] = [y for y in data[i][0]]

# There is only 1 time and 1 distance
# So we had to concatenate the 2 lists of str to have 1 variable for each
time = ""
for x in data[0]:
    time = time + x
time = int(time)
print(time)

distance = ""
for x in data[1]:
    distance = distance + x
distance = int(distance)
print(distance)

# Calculate the number of differents ways to beat the record
x = 0
total = 0
while x < time:
    timeleft = time - x
    if (x * timeleft) > distance:
        total += 1
    x += 1
print(f"There is {total} differents way to beat the record of {distance} millimeters")

print(total)
