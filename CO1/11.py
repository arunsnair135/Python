print("Enter the 3 numbers")
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
if((a>b)and(a>c)):
    print("First number is the largest")
elif((b>a)and(b>c)):
    print("Second number is the largest")
elif((c>a)and(c>b)):
    print("Third number is the largest")
