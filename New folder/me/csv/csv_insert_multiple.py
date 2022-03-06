import csv

with open("details.csv","r") as f:
	print(f.read())

with open("details.csv","a") as f:
	write_obj=csv.writer(f)
	l=[]
	q=[]
	r=int(input("Enter number of Entries"))
	for i in range(0,r):  
 		l.append([input() for j in range(0,2,1)]) 
	write_obj.writerows(l)
	
with open("details.csv","r") as f:
	print(f.read())

