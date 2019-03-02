# Take numbers from user until 0 is entered and display sum of numbers

sum = 0
while True:
    num = int(input("Enter a number :"))
    if num == 0:
        break

    sum += num

print(sum)
