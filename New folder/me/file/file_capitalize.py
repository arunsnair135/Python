f=open("lines.txt","r")
l=f.readlines()
f2=open("l2.txt","w")
for i in l:
	f2.write(i.capitalize())

f.close()
f2.close()
f2=open("l2.txt","r")
for i in f2:
	print(i)
