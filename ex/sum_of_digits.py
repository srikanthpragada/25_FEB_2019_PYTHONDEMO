# Program to sum unique digits of five numbers

digits = set()
for i in range(1,6):
    num = int(input("Enter a number :"))
    while num > 0:
        digit = num % 10
        digits.add(digit)
        num //= 10


print("Sum of digits = ", sum(digits))