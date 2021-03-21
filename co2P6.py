s=input("enter a string:")
count=0
for i in range(len(s)):
    if(s[i]!=' '):
        count=count+1
print("total number of characters in the string:",count)