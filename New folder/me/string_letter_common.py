
s=input("Enter the text")
w=s.split(' ')

for i in w:
	c=0
	for j in w:
		if i==j:
			c+=1
	print("Occurance of",i,c)
	
