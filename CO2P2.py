n=int(input("enter number of terms:"))
a=0
b=1
if(n<=0):
    print("enter a positive integer:")
elif(n==1):
    print(a)
else:
    for i in range(n+1):
        print(a)
        i=a+b
        a=b
        b=i