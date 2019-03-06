teldir = {}  # Empty dict

while True:
     name = input("Enter name [end to stop] : ")
     if name == 'end':
         break

     mobile = input("Enter mobile number  : ")
     teldir[name] = mobile  # insert into dict


for n,m in sorted(teldir.items()):
    print(f"{n:15}:{m} ", end=' ')
