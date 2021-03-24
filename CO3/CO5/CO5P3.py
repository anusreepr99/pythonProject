import csv
l=[]
with open("class.csv","w") as csvfile:
    write=csv.writer(csvfile)
    write.writerow(["slno","name","grade"])
    write.writerow(["1","Anu","A"])
    write.writerow(["2","Sree","B"])
    write.writerow(["3","Nandu","B"])
with open("class.csv") as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        l.append(row)
        print(row)
print(l)