# Simple calculator v1
from colorama import init
from colorama import Fore, Back, Style

init()
print(Back.RED)
print(Fore.BLACK)
print("Hello!")
what = input("What are we doing? (+ or -)")

print(Back.YELLOW)

a = float( input("Enter the first number: "))
b =  float ( input("Enter the second number: "))

print(Back.MAGENTA)
if what == "+":
    c = a + b
    print("Result: " + str(c))

elif  what == "-":
    c = a - b
    print("Result: " + str(c))
else:
    print("Wrong operation selected")

input()