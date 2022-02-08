f1=open("des.txt","w")
f2=open("sou.txt","r")
l=f2.readlines()
for j in range(0,len(l)):
	if(j%2==0):
		f1.write(l[j])
f1.close()
f2.close()
