def merge(dict1,dict2):
    return(dict1.update(dict2))
dict1={'a':2,'b':4}
dict2={'c':6,'d':8}
print(merge(dict1,dict2))
print(dict1)