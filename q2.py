f=open("myfile.txt","r")
l=[]
out=[]
for i in f:
	if(i=="\n"):
		continue
	else:
		l.append(i)
print("****Original File Content****")
for i in l:
	print(i)
for i in l:
	if(len(i.split())>=5):
			if(i[0].isupper()):
				out.append(i)
				break
print("****OUTPUT****:")
for i in out:
	print(i)
f.close()
