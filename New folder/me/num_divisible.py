x=int(input("Enter the last number"))
l=[]
i=0
while i<=x:
	if(i%5==0):
		l.append(i)
	i+=1
print(l)
