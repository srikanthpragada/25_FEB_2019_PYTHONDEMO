elist = []
olist = []

while True:
     num = int (input("Enter a number [0 to stop] :"))
     if num == 0:
         break

     if num % 2 == 0:
         elist.append(num)
     else:
         olist.append(num)


for n in  elist + olist:
    print(n)



