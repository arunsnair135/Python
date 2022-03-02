s=int(input("enter the num"))
r=0
sum=0
while(s>0):
    r=s%10
    sum+=r
    s=s//10
print("sum",sum)
    
