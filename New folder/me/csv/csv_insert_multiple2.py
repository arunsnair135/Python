import csv

with open("details.csv","r") as f:
	print(f.read())

with open("details.csv","a") as f:
	write_obj=csv.writer(f)
	l=[
	   ["Amal",24],
	   ["Anson",22]]
	write_obj.writerows(l)

with open("details.csv","r") as f:
	print(f.read())
	
