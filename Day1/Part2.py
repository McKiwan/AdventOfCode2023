# ADVENT OF CODE 2023
# --- Day 1: Trebuchet?! ---
# https://adventofcode.com/2023/day/1#part2
# --- Part Two ---
import pandas as pd
import regex as re

DATA_PATH = "input.txt"

# Read the input file
df = pd.read_csv(DATA_PATH, header=None)
data = df[0].tolist()

# Dictionary to replace the words with numbers
numbers_dic = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


# Replace the words with numbers
def replace_numbers(word):
    for key, value in numbers_dic.items():
        word = word.replace(key, value)
    return word


# Find all occurences of numbers spelled or in digits in each line using regex
r = [
    re.findall(
        r"\d|one|two|three|four|five|six|seven|eight|nine", line, overlapped=True
    )
    for line in data
]

# Calculate the total sum of the first and last number in each line
print(sum(int(replace_numbers(x[0]) + replace_numbers(x[-1])) for x in r))
