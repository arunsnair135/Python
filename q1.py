import csv
with open("marks.csv","a")as f:
	l=[	["Adharsh",70,88,45,90],
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
	#wr.writerows(l)
f.close()
with open("marks.csv","r")as f:
	reader=csv.reader(f)
	l=list(reader)
	per=[]

	mfc=ase=dc=ds=0
	limiter=0
	for i in l:
		if(limiter==0):
			limiter=1
		else:
			p=int(i[1]) + int(i[2]) +int(i[3])
			p=int((p/400)*100)
			per.append(p)
			mfc=mfc+int(i[1])
			dc=dc+int(i[1])
			ds=ds+int(i[1])
			ase=ase+int(i[1])
f.close()
with open("marks.csv","r")as f:
	for_per=-1
	field=0
	for i in f:
		print("\n")
		print(i)
		if(for_per==-1):				
			for_per+=1
		else:
			print("percentage=",per[for_per])
			print("***")
			for_per+=1
print("\nSubjectwise Average")
print("MFC",mfc/10)
print("DC",dc/10)
print("DS",ds/10)
print("ASE",ase/10)
f.close()
