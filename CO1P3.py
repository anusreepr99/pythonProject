#positive list of numbers from a given list integers
a=[-3,-2,-1,1,2,3]
b=[x for x in a if x>0]
print(b)
#square of N numbers
n=int(input("enter the number of numbers:"))
list=[]
for i in range(n):
    x=int(input("enter the number:"))
    list.append(x)
print(list)
newlist=[x**2 for x in list]
print(newlist)
#list of vowels
vowels="aeiou"
word=input("enter a word:")
list=[x for x in  word if x in vowels]
print(list)
#ordinal value of each element of a word
word=input("enter a word:")
list=[ord(x) for x in word]
print(list)