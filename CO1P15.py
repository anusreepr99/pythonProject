l1=['red','blue','yellow']
l2=['pink','violet','blue']
print(l1)
print(l2)
for x in (l1):
    for y in (l2):
        if x==y:
         l1.remove(x)
print("the colours not in col2 are:",l1)
