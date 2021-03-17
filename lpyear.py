c=int(input("Enter current year:"))
f=int(input("enter a year:"))
for i in range(c,f):
    if(i%4==0 or i%100==0 or i%400==0):
        print(i)
        i=i+1