s=input("Enter the text")
w=s.split(' ')
c={}
for w in w:
    c[w]=c.get(w,0)+1
print(c)
