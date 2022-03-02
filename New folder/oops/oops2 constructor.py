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
    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"destroyed")
s1=student(1,"abhi","mca")
s2=student(2,"amal","mca")
s1.display()
s2.display()
student.displaycount()
del s1





