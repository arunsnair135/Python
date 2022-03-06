x=eval(input("Enter the number"))
s=0;
r=0
while x>0:
	r=x%10
	s+=r
	x=x//10
print(s)
