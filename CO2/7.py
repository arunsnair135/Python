s=input("Enter the string")
l=len(s)
l=l-3
b=s[0:l]
e=s[-3:]
n1="ly"
n2="ing"
if(e=='ing'):
    print(b+n1)
else:
    print(s+n2)

    
