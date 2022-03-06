x=int(input("Enter the limit"))
a,b=0,1
l=[]
l.append(a)
l.append(b)
c=2
while c<x:
	c=a+b
	l.append(c)
	a,b=b,c
	c=c+1
print(l)

	
