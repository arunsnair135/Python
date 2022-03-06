import csv

with open("file.csv","w")as f:
	l=[	["Name","MFC","DC","DS","ASE"],
		["Adharsh",70,88,45,90],
		["Arun",67,80,70,50],
		["Binoy",78,90,100,89],
		["Chandrakanth",89,66,56,45],
		["Don",90,89,78,90],
		["Afeef",70,58,95,90],
		["Shibli",68,80,70,40],
		["Arjun",78,45,80,89],
		["Marvin",89,100,60,45],
		["Shiavashankar",90,100,78,90]	]
	
	wr=csv.writer(f)
	wr.writerows(l)

with open("file.csv","r")as f:
	rd=csv.reader(f)
	header=next(rd)
	print(header)
	l=[]
	for i in rd:
		l.append(i)
		
	for i in l:
		print(i)
		
	mfc=(sum(int(i[1]) for i in l))/10
	dc=(sum(int(i[2]) for i in l))/10
	ds=(sum(int(i[3]) for i in l))/10
	ase=(sum(int(i[4]) for i in l))/10
	per=[]
	for i in l:
		p=int(i[1])+int(i[2])+int(i[3])+int(i[4])
		per.append(int(p/4))
	for i in per:
		print(i)
	l=[x+y for x,y in zip(l,per)]

	print("Result")
	for i in l:
		print(i)
		
