import random
import sys
print("Welcome to guess the number.")
def howtoplay():
    print("Version 1: The computer comes up with a number between 0-100 and gives you hints to help you guess it.")
    print("Version 2: You think of a number between 0-100 and give the computer clues to help it guess your number.")
def vone():
    x = (random.randint(0,100))
    print("Press q to exit.")
    y = input("Guess a number here: ")
    while x != y: 
        if y == 'q':
            break
        elif int(y) > x:
            y =int(input("Guess lower: "))
        elif int(y) < x:
            y = int(input("Guess higher: "))
        if x == y:
            print("You guessed the number!")
        break
def vtwo():
    if t == '2':
        print("Welcome to guess the number v2.0")
        print ("Think of a number between 1 and 100")
        low = 0
        high = 100
        while True:
                guess = random.randint(low,high)
                print(guess)
                clue = input("Enter higher, lower, or correct: ")
                if clue == 'higher':
                   low  = guess + 1
                if clue == "lower":
                    high = guess - 1
                if clue == "correct":
                    print("I guessed it right!")
                    break
while True:
    t = input("Enter 1 for version 1 and 2 for version 2 or 'how to play' to learn how to play (press 'e' to exit): ")
    if t == 'e':
        sys.exit()
    elif t == '1':
        vone()
    elif t == '2':
        vtwo()
    elif t ==  'how to play':
        howtoplay()
     

    
