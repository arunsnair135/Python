import csv
print("I")
with open("details.csv","r") as f: 
	print(f.read())
f.close()
print("II")
with open("details.csv","r") as f: 
	read_obj=csv.reader(f)
	l=read_obj
	for i in l:
		for j in i:
			print(j)
f.close()

print("III")
with open("details.csv","r") as f: 
	read_obj=csv.reader(f)
	l=read_obj
	
	for i in l:
		c=1
		for j in i:
			if c==1:
				c+=1
			else:
				print(j)
				
print("IV")
with open("details.csv","r") as f: 
	read_obj=csv.reader(f)
	l=read_obj
	for j in l:
		print(j)

f.close()
