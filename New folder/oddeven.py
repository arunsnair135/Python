l=[1,5,6,4,44,8,7,1]
even=[]
odd=[]
for i in l:
    if i%2==1:
        odd.append(i)
    else:
        even.append(i)
print("Odd:",odd)
print("Even:",even)
