import random
print("Welcome to guess the number v2.0")
print ("Think of a number between 1 and 100")
low = 1
high = 100
while True:
    guess = random.randint(low,high)
    print(guess)
    clue = input("Enter higher, lower, or correct: ")
    if clue == 'higher':
        low = guess
    if clue == "lower":
        high = guess
    if clue == "correct":
        print("I guessed it right!")
        break
    
    
