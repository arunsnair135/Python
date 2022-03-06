import csv

with open("details.csv","r") as f:
	print(f.read())



with open("details.csv","a") as f:
	write_obj=csv.writer(f)
	l=[]
	l.append(input("Enter name"))
	l.append(int(input("Enter age")))
	write_obj.writerow(l)
	


with open("details.csv","r") as f:
	print(f.read())

