# ADVENT OF CODE 2023
# --- Day 7: Camel Cards ---
# https://adventofcode.com/2023/day/7#part2
# --- Part Two ---
import pandas as pd

CARD_PER_HAND = 5

# Read the input file
df = pd.read_csv("input.txt", sep=" ", header=None, names=["Hands", "Bids"])
hands = df["Hands"].tolist()

# Card in order : A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J
# Hand in order :
## Five of a kind (AAAAA)
## Four of a kind (AAAAx)
## Full house (AAAKK)
## Three of a kind (AAAxx)
## Two pair (AAKKx)
## One pair (AAxxx)
## High card (AKQJT)


# Strenght value of a card (J is now Joker but has the lowest value)
def card_value(card):
    if card == "A":
        return 14
    elif card == "K":
        return 13
    elif card == "Q":
        return 12
    elif card == "J":
        return 1
    elif card == "T":
        return 10
    return int(card)


# Compare two cards and return the one with the highest value
def higher_card(card_one, card_two):
    if card_one == card_two:
        return None
    elif card_value(card_one) > card_value(card_two):
        return card_one
    return card_two


# Return the value of a hand
# Joker is whatever card which will make the hand the highest possible
def hand_value(hand):
    values = [card_value(card) for card in hand]
    counts = {value: values.count(value) for value in values}
    nb_joker = hand.count("J")
    if 5 in counts.values():
        return "Five of a kind"
    elif 4 in counts.values():
        if nb_joker == 1 or nb_joker == 4:
            return "Five of a kind"
        return "Four of a kind"
    elif set(counts.values()) == {3, 2}:
        if nb_joker == 2 or nb_joker == 3:
            return "Five of a kind"
        return "Full house"
    elif 3 in counts.values():
        if nb_joker == 3 or nb_joker == 1:
            return "Four of a kind"
        return "Three of a kind"
    elif list(counts.values()).count(2) == 2:
        if nb_joker == 2:
            return "Four of a kind"
        elif nb_joker == 1:
            return "Full house"
        return "Two pair"
    elif 2 in counts.values():
        if nb_joker == 1 or nb_joker == 2:
            return "Three of a kind"
        return "One pair"
    else:
        if nb_joker == 1:
            return "One pair"
        return "High card"


# Compare two hands and return the one with the highest value
def higher_hand(hand_one, hand_two):
    hand_value_dic = {
        "Five of a kind": 6,
        "Four of a kind": 5,
        "Full house": 4,
        "Three of a kind": 3,
        "Two pair": 2,
        "One pair": 1,
        "High card": 0,
    }

    value_one = hand_value_dic.get(hand_value(hand_one), -1)
    value_two = hand_value_dic.get(hand_value(hand_two), -1)

    if value_one > value_two:
        return hand_one
    elif value_two > value_one:
        return hand_two
    else:
        i = 0
        while i < CARD_PER_HAND:
            card_one = hand_one[i]
            card_two = hand_two[i]
            if higher_card(card_one, card_two) == card_one:
                return hand_one
            elif higher_card(card_one, card_two) == card_two:
                return hand_two
            i += 1


# Sort the hands by value
def sort_hand(hands, df):
    n = len(hands)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if higher_hand(hands[j], hands[j + 1]) == hands[j]:
                hands[j], hands[j + 1] = hands[j + 1], hands[j]
                df.iloc[j], df.iloc[j + 1] = df.iloc[j + 1], df.iloc[j]
                already_sorted = False
        if already_sorted:
            break
    return df


# Calculate the score for the exercise
def calculate_score(df):
    score = 0
    i = 0
    while i < len(df):
        score += (i + 1) * df.iloc[i]["Bids"]
        i += 1
    return score


sort_hand(hands, df)
print(calculate_score(df))
