f = open("story.txt","rt")
words = set()

for line in f:
    wrds = line.strip("\n").split(" ")
    for w in wrds:
        if len(w.strip()) > 0:
           words.add(w)


print (sorted(words))
