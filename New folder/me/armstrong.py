x=int(input("Enter the number"))
n=x
s=0
i=0
while x>0:
	i=x%10
	x=x//10
	s=s+i**3
if(s==n):
	print("IS ARMSTRONG")
else:
	print("NOT ARMSTRONG")	
