f=open("lines.txt","r")
l=f.readlines()
b=0

#line
for i in l:
	if len(i)>b:
		b=len(i)
		s=i
print(s)


#word
for i in l:
	c=i.split()
	for j in c:
		if len(j)>b:
			b=len(j)
			s=j
print(s)

f2.close()
