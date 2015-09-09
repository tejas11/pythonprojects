import random
import sys
print("Welcome to dice rolling simulator!")
while True:
    y = input("Press 'y' to roll or press 'e'  to exit: ")
    z = 1
    a = 0
    while y == 'y' and a < 1:
        x = random.randint(1,6)
        print("You rolled a %(x1)d." %
            {'x1':x})
        a = z 
    while y == 'e':
        sys.exit()



