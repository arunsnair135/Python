import csv
with open("mark.csv","r") as f1:
	read_obj=csv.reader(f1)
	l=read_obj
	for j in l:
		print(j)
		
