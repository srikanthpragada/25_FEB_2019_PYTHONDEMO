# Take a number from user and display whether it is even number
import sys

# for i in range(1, len(sys.argv)):
#     num = int( sys.argv[i])


for n in sys.argv[1:]:
    num = int(n)
    if num % 2 == 0:
        print(f"{num} is even number")
    else:
        print(f"{num} odd number")
