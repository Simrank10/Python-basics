"""
Project: Rock, Paper, Scissors Game
Write a Python program where:
The user chooses Rock (0), Paper (1), or Scissors (2).
The computer randomly selects one of the three options.

Display both the user and computer choices using ASCII art.

Determine the winner:
1. Rock beats Scissors
2. Scissors beats Paper
3. Paper beats Rock

Display the result: You win!, Computer wins!, or It's a tie!

"""


Rock = '''
    _______
---'   ____)____
          (_____)
          (_____)
          (____)
---.__(___)
    ROCK
'''  # Representing a clenched fist

Paper = '''
    _______
---'   ____)____
          ______)
         _______)
        _______)
---.__________)
       |       |
       | PAPER |
       |_______|
'''  # Representing an open hand

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    SCISSORS
'''  # Two fingers extended

rps = int(input("Select Rock(0), Paper(1) or Scissors(2) : "))
rps_list = [Rock, Paper, Scissors]

if rps>= 3 or rps<0:
    print("Invalid input")
else:
    print(f"you selected : {rps_list[rps]}")

import random
comp_rps = random.randint(0, 2)
#print(comp_rps)
print(f"comp selected : {rps_list[comp_rps]}")

if rps == comp_rps:
    print("It's a tie!")
elif (rps==0 and comp_rps==2) or (rps==1 and comp_rps==0) or (rps==2 and comp_rps==1):
    print('You won!')
else:
    print("Computer wins!")