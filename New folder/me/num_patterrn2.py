x=int(input("Enter the limit"))
for i in range(1,x+1,1):
	for j in range(1,i+1,1):
		print(j,end=" ")
	print()
for i in range(x-1,0,-1):
	for j in range(1,i+1,1):
		print(j,end=" ")
	print()
	

