# Program to print common chars between two strings

s1 = input("Enter first  string : ")
s2 = input("Enter second string : ")

for c in s1:
    if c in s2:
        print(c)


