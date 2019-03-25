
a = 10
b = 0
try:
    c = a/b
    print(c)
except Exception as ex:
    print(type(ex))
    print(ex)
else:
    print("Done")
finally:
    print("The End")

print("Over")


