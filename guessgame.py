from pydoc import importfile


import random

randomNo= random.randint(1,20)
# print(randomNo)
myguess=None
guess=0

while myguess != randomNo:
    mynumber=int(input("Enter a Number: "))
    if randomNo==mynumber:
        print("You Guessed It Right! ")
    else:
        if mynumber<randomNo:
            print("You Guessed It Wrong! Pick Higher No ")
        else: 
            print("You Guessed It Wrong! Pick Lower No ")
guess = guess + 1

print(f"You Guessed No in {guess} guesses ")