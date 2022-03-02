n=int(input("Enter the number of stars in the middle"))
for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        print("*",end=" ")
    print()
for i in range(i-1,0,-1):
    for j in range(1,i+1,1):
        print("*",end=" ")
    print()
    
