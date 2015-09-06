import random
import sys
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
    sys.exit()
    
        

