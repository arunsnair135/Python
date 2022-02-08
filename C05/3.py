import csv
with open("myfile.csv","r") as f:
	r=csv.reader(f)
	l=list(r)
	for i in l:
		print(i)
f.close()
