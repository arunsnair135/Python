f=open("lines.txt","r")
l=f.readlines()
f2=open("uppercopy.txt","w")
w=[]
for i in l:
	if i[0].isupper():
		f2.write(i)
			
			
f.close()
f2.close()

f2=open("uppercopy.txt","r")
for i in f2:
	print(i)
f2.close()


#for i in l:
	
	#f2.write(i.title())
			
			
