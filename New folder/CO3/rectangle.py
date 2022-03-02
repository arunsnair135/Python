class rectangle:
    def insert(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        self.a=self.l*self.b
    def perimeter(self):
        self.p=2*(l+b)
    def display(self):
        print("Area: ",self.a)
        print("Perimeter: ",self.p)
n=int(input("Enter the number of rectangle "))
list=[]
for i in range(1,n+1):
    list.append(rectangle())
k=1
for i in list:
    print("Rectangle",k)
    l=int(input("Enter the Length of rectangle"))
    b=int(input("Enter the breadth of  rectangle"))
    i.insert(l,b)
    i.area()
    i.perimeter()
    k+=1
for i in list:
    i.display()






    
   

