import math
start,limit=int(input("Start")),int(input("Limit"))
main=[]
count=0
for i in range(start,limit+1,1):
    sr=math.sqrt(i)
    if int(sr+0.5)**2==i:
        num=i
        while(num>0):
            d=num%10
            if(d%2==0):
                count=count+1
            num=num//10
        if(count==4):
            main.append(i)
    count=0
print(main)
