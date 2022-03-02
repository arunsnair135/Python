s=input("enter the string")
i=int(input("enter the index of character to be deleted"))
i=i-1
f=s[0:i]
j=i+1
l=s[j:]
print(f+l)

