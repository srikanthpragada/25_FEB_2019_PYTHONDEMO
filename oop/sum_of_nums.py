sum = 0
for i in range(1, 6):
    try:
        num = int(input("Enter number :"))
        sum += num
    except:
        pass

print(f"Sum = {sum}")
