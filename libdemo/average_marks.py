with open("marks.txt", "rt") as f:
    marks = []
    for line in f.readlines():
        marks.append(int(line))

    print("Average : ", sum(marks) / len(marks))
