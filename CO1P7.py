list1=[1,2,3,4,5]
list2=[2,4,6,8,10,12]
print("elements in first list are:",list1)
print("elements in second list are:",list2)
if(len(list1)==len(list2)):
    print("lists having same length")
else:
    print("lists have different length")
s1=0
s2=0
for i in range(len(list1)):
    s1=s1+list1[i]
print("sum of list1:",s1)
for i in range(len(list2)):
    s2=s2+list2[i]
print("sum of list2:",s2)
print("the common elements are:")
for i in list1:
  for j in list2:
    if i==j:
        print(i)