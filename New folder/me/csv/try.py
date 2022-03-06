import csv
dict1=[	{"No":1,"Name":"Amal","Age":21},
      	{"No":2,"Name":"Arun","Age":21},
     	{"No":1,"Name":"Jinu","Age":21}	]

field=["No","Name","Age"]

with open("dictionary1.csv","w") as f:
	
	write_obj=csv.DictWriter(f,fieldnames=field)
	write_obj.writeheader()
	write_obj.writerows(dict1)
with open("dictionary1.csv","r") as f:
	read_obj=csv.reader(f)
	for i in read_obj:
		print(i)
