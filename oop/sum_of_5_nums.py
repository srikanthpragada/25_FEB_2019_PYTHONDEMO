sum = 0
i = 1
while i <= 5:
    try:
        num = int(input("Enter number :"))
        sum += num
        i += 1
    except (ValueError, OverflowError) as e:
        print(e)
    except ZeroDivisionError as e:
        pass

print(f"Sum = {sum}")
