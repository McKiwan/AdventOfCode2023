# ADVENT OF CODE 2023
# --- Day 15: Lens Library ---
# https://adventofcode.com/2023/day/15
# --- Part One ---
# Read the input file
with open("input.txt") as f:
    data = f.read().strip()


data = data.strip().split(",")

# Calculate the hash value of each sequence
ans = 0
for sequence in data:
    cur_val = 0
    for char in sequence:
        cur_val += ord(char)
        cur_val *= 17
        cur_val %= 256
    ans += cur_val

# Print the total which is the sum of all hash values
print(ans)
