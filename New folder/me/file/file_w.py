f=open("demo.txt","w")
for i in range(1,11,1):
	f.write(str(i))
	f.write("\n")
f.close()
