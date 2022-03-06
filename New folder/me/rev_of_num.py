x=int(input("Enter the number"))
r=0;
while x>0:
	r=(r*10)+(x%10)
	x=x//10
print(r)
