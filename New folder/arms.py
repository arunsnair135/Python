def arms(n):
    temp = n
    sum1 = 0      
    while (temp != 0):
       digit=temp%10
       sum1+=digit**3
       temp=temp//10
    if sum1==n:
        print("Is an armsstong num")
    else:
        print("Not an armsstong num")
  

n=int(input("Enter the number"))
arms(n)
