def q():
	f=open("demo.txt","r")
	s=0
	for i in f:
		s+=int(i)
	print(s)
	f.close()

