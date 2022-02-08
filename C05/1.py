f=open("1.txt","r")
l=[]

#to list
for i in f:
	l.append(i)

for i in l:
	print(i)

#print(f.read())
f.close()
