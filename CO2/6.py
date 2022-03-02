s=input("Enter the text")
c={}
for i in s:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)
    
