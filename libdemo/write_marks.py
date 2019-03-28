
with open("marks.txt","wt") as f:
  while True:
    m = int(input("Enter marks [0 to stop] :"))
    if m == 0:
        break
    f.write(str(m) + "\n")

