# Print union of chars in 5 strings
chars = []

for i in range(1,6):
    st = input("Enter a string :")
    for ch in st:
        if ch not in chars:
            chars.append(ch)


print(chars)
