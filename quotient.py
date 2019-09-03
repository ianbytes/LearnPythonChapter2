quotient = 0
remainder = 0

x = int(input("Give me a number:"))
y = int(input("Give me a 2nd number:"))

if y == 0:
    print("The world ends when I divide by zero")
else:
    quotient = x / y
    remainder = x % y
    print("The quotient of",x,"and",y,"is",int(quotient),"with a remainder of",remainder)




