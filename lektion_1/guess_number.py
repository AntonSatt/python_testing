#This is a program to guess the number

import random

random_number = random.randint(1,101)

number_guess = int(input("Guess the number from 1-100 "))

if number_guess == random_number:
    print("You got the number!")
else:
    print("You failed!")