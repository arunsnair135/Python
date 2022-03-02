l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=input("String:")
count=0
for i in s:
    for j in l:
        if j==i:
            count=count+1
if(count>=26):
    print("pangram")
else:
    print("Not Pangram")
