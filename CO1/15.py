s=input("enter the colours in L1")
s1=input("enter the colours in L2")
s2=s.split(" ")
s3=s1.split(" ")
s4=set(s2)-set(s3)
print(s4)
