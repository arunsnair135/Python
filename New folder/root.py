import math
l=[]
k=[]
ll=[]
flag=0
for i in range (100):
    s=math.sqrt(i)
    s=math.floor(s)
    if(s*s==i):
        l.append(i)
print("nums=",l)
if i in l:
    if(i%2==0):
        print(y)
print("nums=",ll)



for i in l:
     while(i>0):
         print(i)
         q=i
         if(i%2==1):
             flag=1
             break
         else:
            if(i<10):
                k.append(q)
                i=0
            else:
                i=i//10  
print("nums=",k)
    

    
