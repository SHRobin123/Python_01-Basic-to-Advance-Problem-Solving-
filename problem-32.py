#Number Guessing Game
import random

# computer generates a random number between 1 to 10
secret_number = random.randint(1, 10)

guess = int(input("Guess a number (1 to 10): "))

if guess == secret_number:
    print("Correct! You guessed it right.")
else:
    print("Wrong! The correct number was:", secret_number)

'''
output:-

Guess a number (1 to 10): 5
Wrong! The correct number was: 8
'''