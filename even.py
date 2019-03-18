# Take a number from user and display whether it is even number
import sys

if len(sys.argv) == 1:
    print("Usage : python even.py number")
    sys.exit(1)   # Stop program


num=int(sys.argv[1])

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")