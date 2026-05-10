#Rock Paper Scissors

import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)

user = input("Enter rock, paper or scissors: ").lower()

print("Computer choice:", computer)
print("Your choice:", user)

if user == computer:
    print("Draw!")
elif (user == "rock" and computer == "scissors") or \
     (user == "scissors" and computer == "paper") or \
     (user == "paper" and computer == "rock"):
    print("You Win!")
else:
    print("You Lose!")

'''
output:-

Enter rock, paper or scissors: rock
Computer choice: scissors
Your choice: rock
You Win!
'''