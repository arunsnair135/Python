x=int(input("Enter the number"))
l=[]
s=0
for i in range(1,x+1,1):
	if(i%2==0):
		l.append(i)
		s+=i
print(l,s)
