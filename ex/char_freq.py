
sen = input("Enter a sentence : ")
freq = {}

for c in sen:
    if c in freq:
        freq[c] = freq[c] + 1
    else:
        freq[c] = 1


for c,cnt in freq.items():
    print(c, cnt)

