list=[]
colours=input("enter list of colours:")
c=colours.split(",")
for i in c:
    list.append(i)
print(list)
print("first colour is:",list[0])
print("last colour is:",list[-1])