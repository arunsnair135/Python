square=lambda a:a*a
triangle=lambda b,h:0.5*b*h
rectangle=lambda l,b:l*b
s=int(input("Enter the side of the square"))
r1=square(s)
t1=int(input("Enter the b of the triangle"))
t2=int(input("Enter the heigth of the triangle"))
r2=triangle(t1,t2)
rec1=int(input("Enter the heigth of the rectangle"))
rec2=int(input("Enter the breadth of the rectangle"))
r3=rectangle(rec1,rec2)
print("Square=",r1)
print("Triangle=",r2)
print("rectangle=",r3)