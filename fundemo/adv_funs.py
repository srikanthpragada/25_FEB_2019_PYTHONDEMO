
def process():
    print("Processing")


process()
print(type(process))
calculate = process
calculate()
print(type(calculate))
print(process == calculate)