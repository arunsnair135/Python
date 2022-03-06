import csv
with open("mark.csv","r") as f:
	reader_obj=csv.reader(f)
	header=next(reader_obj)
	l=[]
	print(header)
	for i in reader_obj:
		l.append(i)
	for i in l:
		print(i)
