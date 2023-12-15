# ADVENT OF CODE 2023
# --- Day 15: Lens Library ---
# https://adventofcode.com/2023/day/15#part2
# --- Part Two ---
# Calculate the hash value of each sequence
def hash(sequence):
    cur_val = 0
    for char in sequence:
        cur_val += ord(char)
        cur_val *= 17
        cur_val %= 256
    return cur_val


# Read the input file
with open("input.txt") as f:
    data = f.read().strip()

data = data.strip().split(",")

# Create a list of 256 empty lists
box = [[] for _ in range(256)]

# Each sequence is a lens
# The value of the lens is the number after "=" that we call focal length
# Store the lens in the corresponding list in the box
# If the sequence contains "=", replace the lens or append it
# If the sequence contains "-", remove the corresponding lens
for sequence in data:
    if "=" in sequence:
        label, value = sequence.split("=")
        if box[hash(label)] == []:
            box[hash(label)].append(f"{label} {value}")
        else:
            for i, item in enumerate(box[hash(label)]):
                rewrite = False
                if item.startswith(label):
                    box[hash(label)][i] = f"{label} {value}"
                    rewrite = True
                    break
            if not rewrite:
                box[hash(label)].append(f"{label} {value}")

    elif "-" in sequence:
        label = sequence.split("-")[0]
        for i, item in enumerate(box[hash(label)]):
            if item.startswith(label):
                box[hash(label)].pop(i)

# Calculate the total
# The total is the sum of the following values for each lens:
## One plus the box number of the lens in question.
## The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
## The focal length of the lens.
total = 0
for i, sublist in enumerate(box):
    if sublist:
        for index, item in enumerate(sublist):
            value = 0
            value += (i + 1) * (index + 1) * int(item.split()[1])
            total += value

print(total)
