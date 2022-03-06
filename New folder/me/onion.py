s=input("Enter the text ")
q=s[1:]

#print(s[0],end="")

#for i in q:
#	if i==s[0]:
#		print("$",end="")
#	else:
#		print(i,end="")

print(s[0]+s[1:].replace(s[0],'$'))
