import random

# Super simple Rock, Paper, Scissors game...

# User chooses r p or s
user_choice = input("Enter r, p, or s for rock paper or scisors: ")

# Computer choice randomly generated
computer_choice = random.choice(["r", "p", "s"])

print(f'You chose: {user_choice} and the computer chose {computer_choice}; therefore...\n')

# Programmer must code the tie, win lose messages based on his choice...

if user_choice == computer_choice:
    print("You tied!")
elif user_choice == 's':
    print("You lose!")
elif user_choice == "p" and computer_choice== "s" or user_choice== "p" and \
      computer_choice == "r" or user_choice == "s" and computer_choice == "p":
    print("You win!")
