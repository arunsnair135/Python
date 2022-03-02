def longestlength(a):
    max1=len(a[0])
    for i in a:
        if(len(i)>max1):
            max1=len(i)
            temp=i
    print("Longest word is ",temp,"and length is",max1)
a=[]
n=int(input("Enter the number of words:"))
for x in range(0,n):
    val=input()
    a.append(val)
longestlength(a)
