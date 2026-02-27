import random

choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)

pick = input("Enter your choice --> ")

"""
0: Rock
1: Paper
2: Scissors

LOGIC (B = BEATS)

0 B 2
1 B 0
2 B 1
"""

if computer == choices[0] and pick == choices[2]:
    print(f'{choices[0]} beats {choices[2]}! You lose!')

elif computer == choices[2] and pick == choices[1]:
    print(f'{choices[2]} beats {choices[1]}! You lose!')

elif computer == choices[1] and pick == choices[0]:
    print(f'{choices[1]} beats {choices[0]}! You lose!')

elif computer == choices[2] and pick == choices[0]:
    print(f'{choices[0]} beats {choices[2]}! You win!')

elif computer == choices[1] and pick == choices[2]:
    print(f'{choices[2]} beats {choices[1]}! You win!')

elif computer == choices[0] and pick == choices[1]:
    print(f'{choices[1]} beats {choices[0]}! You win!')

else:
    print("Put a valid option.")




