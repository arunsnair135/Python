class student:
    stcount=0
    def getdata(self,roll,name,course):
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
s1=student()
s2=student()
s1.getdata(1,"abhi","mca")
s2.getdata(2,"amal","mca")
s1.display()
s2.display()
student.displaycount()
