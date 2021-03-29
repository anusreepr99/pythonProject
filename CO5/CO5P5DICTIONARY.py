import csv
header=["place","name","age"]
with open("city.csv","w") as csvfile:
    write=csv.DictWriter(csvfile,fieldnames=header)
    write.writeheader()
    limit=int(input("enter the numbr of lines u want to enter:"))
    for i in range(limit):
        row_str=input("enter the data inorder(place,name,age) seperated by comma:")
        row_lst=row_str.split(",")
        write.writerow({"place":row_lst[0],"name":row_lst[1],"age":row_lst[1]})
    with open("city.csv","r") as csvfile:
        read=csv.DictReader(csvfile)
        for i in read:
            print(dict(i))
