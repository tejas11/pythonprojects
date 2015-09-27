import random
print("Welcome to dice rolling simulator")
def dice(number_of_dice):
    for i in range(0,number_of_dice):
        yield random.randint(1,6)
def roll():
    return random.randint(1,6)
number_of_dice = int(input("Enter how many dice you want to roll: "))
for i in range(0,number_of_dice):
    print (roll()) 
