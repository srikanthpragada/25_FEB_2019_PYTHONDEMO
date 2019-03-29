with open("marks2.txt", "wt") as f:
    marks = []
    while True:
        m = input("Enter marks [0 to stop] :")
        if m == "0":
            break
        marks.append(m)

    # Write marks into file
    f.write(",".join(marks))
