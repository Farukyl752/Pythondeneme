class Quess:
    def __init__( number):
        number = number

    def check(guess):
        if guess<number:
            return "Too low"
        elif guess>number:
            return "Too high"
        else:
            return "Correct"
import random
number=random.randint(1,100)
guess=0
print("Guess a number between 1 and 100:")

while number!=guess:
    guess=int(input("Your guess:"))
    print(Quess.check(guess))
    
print("Congratulations, you guessed the number!")