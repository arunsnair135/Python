class student:
    stcount=0
    def __init__(self,roll,name,course):
        self.roll=roll
        self.name=name
        self.course=course
        student.stcount=student.stcount+1
    def displaycount():
        print("No of Students:  ",student.stcount)
    def display(self):
        print("Roll no: ",self.roll)
        print("Name: ",self.name)
        print("course:" ,self.course)
        print()
n=int(input("enter the number of students"))
list=[]
for i in range(1,n+1):
    a=input("enter the roll number")
    b=input("enter the name")
    c=input("enter the course")
    list.append(student(a,b,c))
for i in list:
    i.display()






