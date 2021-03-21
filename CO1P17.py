dic={'anu':4,'sree':5,'bhagya':6}
l=list(dic.items())
l.sort()
d=dict(l)
print("ascending order is:",d)
l=list(dic.items())
l.sort(reverse=True)
d=dict(l)
print("descending order is:",d)
