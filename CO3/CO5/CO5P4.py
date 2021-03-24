import csv
header=["place","name","age"]
with open('city.csv',"w") as csvfile:
    write=csv.DictWriter(csvfile,fieldnames=header)
    write.writeheader()
    write.writerow({"place":"vadakara","name":"anu","age":21})
    write.writerow({"place":"koyilandy","name":"bhagya","age":18})
    write.writerow({"place":"kozhikode","name":"anjali","age":19})
with open("city.csv") as csvfile:
    read=csv.DictReader(csvfile)
    n=input("enter the column name u want:")
    for i in read:
        print(i[n])