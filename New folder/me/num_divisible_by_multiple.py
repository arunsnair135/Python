x=int(input("Enter the number"))
l=[]
for i in range(1,x+1,1):
	if(i%3==0 and i%5==0 and i%2==0):
		l.append(i)
print(l)
