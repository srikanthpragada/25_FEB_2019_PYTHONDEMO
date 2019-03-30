f = open("story.txt","rt")
words = {}

for line in f:
    wrds = line.strip("\n").split(" ")
    for w in wrds:
        if len(w.strip()) == 0:
            continue

        w = w.strip(".")
        # Process word
        if w in words:
            words[w] = words[w] + 1  # increment count
        else:
            words[w] = 1   # insert word with count 1


for w,c in sorted(words.items()):
    print (f"{w:10} {c}")
