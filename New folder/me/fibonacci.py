x=int(input("Enter the limit"))
a,b=0,1
l=[]
l.append(a)
l.append(b)
for i in range(0,x,1):
	c=a+b
	l.append(c)
	a,b=b,c
print(l)

	
