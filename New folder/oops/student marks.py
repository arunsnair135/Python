class student:
    def __init__(self,roll,name,m1,m2,m3):
        self.roll=roll
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.total=m1+m2+m3
        self.per=(self.total/300)*100
    def display(self):
        print("Roll no: ",self.roll)
        print("Name: ",self.name)
        print("Total Mark: ",self.total)
        print("Percentage: ",self.per)
n=int(input("enter the number of students"))
list=[]
for i in range(1,n+1):
    print("Details of student",i)
    a=int(input("enter the roll number"))
    b=input("enter the name")
    c=int(input("enter the mark 1"))
    d=int(input("enter the mark 2"))
    e=int(input("enter the mark 3"))
    list.append(student(a,b,c,d,e))
for i in list:
    i.display()
    j+=1







   

