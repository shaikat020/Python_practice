# what is random number module in python
#answer : to generate random numbers
import random # from random import randint

secret= random.randint(1,100) # secret = randint(1,100)
# if not use random
# secret = 42

guess = 0

while True:
    guess= int(input("Enter your guess (1-100): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    elif guess == secret:
        print("Congratulations! You guessed it right.")
        break
    
