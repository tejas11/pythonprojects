print("Enter a number, and we will give you that many numbers of the fibonacci number sequence!")
y = int(input("Enter a number:"))
x = 2
a = 0
b = 0
if x <= 2:
    a = 1
    b = 1
    print(a)
    print(b)
    x = x + 1
while y >= x:
    c = a +b
    a = b
    b = c
    print(c)
    x = x + 1
