"""
Write a Python program to play a coin toss game where the user guesses heads or tails!
"""


import random

heads = 1
tails = 0

heads_or_tails = int(input("Choose : heads or tails? heads - 1 tails - 0 "))
print()

print(f"You choose {heads_or_tails}")
print()

toss = random.randint(0, 1)
print(f"On unbaised toss : {toss}")
print()

if heads_or_tails == toss:
    print(f"Hey, you won!!")
else:
    print("You lost!")
