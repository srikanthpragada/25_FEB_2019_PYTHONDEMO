import sys

filename = input("Enter filename :")
if not filename.endswith('.py'):
    print("Sorry! File must be a .py file!")
    sys.exit(0)
try:
    file = open(filename, "rt")
    # lineno = 1
    # for line in file.readlines():
    #     print(f"{lineno:3}: {line}", end='')
    #     lineno += 1

    for (lineno, line) in enumerate(file):
        print(f"{lineno+1:3}: {line}", end='')

except FileNotFoundError:
    print("Sorry! File not found!")
except:
    print("Sorry! Program terminated due to error!")
