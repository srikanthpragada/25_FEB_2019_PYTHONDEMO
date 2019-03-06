teldir = {}  # Empty dict

while True:
     name = input("Enter name [end to stop] : ")
     if name == 'end':
         break

     mobile = input("Enter mobile number  : ")
     if name in teldir: # name is present in dict
         teldir[name].append(mobile)
     else:
         teldir[name] = [mobile]  # insert into dict


for n,m in sorted(teldir.items()):
    print(f"{n:15} : {m} ")
