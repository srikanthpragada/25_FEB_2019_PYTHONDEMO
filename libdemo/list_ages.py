from datetime import datetime

today = datetime.today()
f = open("dobs.txt", 'rt')

for line in f:
    dobs = line.strip("\n").split(",")
    for dob in dobs:
        try:
            d = datetime.strptime(dob, "%d-%m-%Y")
            age = (today - d).days // 365
            print(f"{d.strftime('%d-%m-%Y')} - {age}")
        except:
            pass

f.close()
