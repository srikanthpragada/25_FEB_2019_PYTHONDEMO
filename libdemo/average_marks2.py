with open("marks2.txt", "rt") as f:
    line = f.readline()
    marks = line.strip("\n").split(",")

    # Convert each string in list to int
    # for i,v in enumerate(marks):
    #     marks[i] = int(v)
    #
    # print("Average : ", sum(marks) / len(marks))

    print("Average : ", sum(map(int,marks)) / len(marks))
