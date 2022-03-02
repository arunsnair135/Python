s=input("enter the string: ")
print(s)
a=s[0]
s=s[1:]
s_new=s.replace(a,'$')
print (a,s_new)
