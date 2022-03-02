class student:
    def __init__(self,r,n,c):
        self.roll=r
        self.name=n
        self.course=c
    def display(self):
        print("Roll no:",self.roll)
        print("Name",self.name)
        print("Course",self.course)
class mark:
    def __init__(self,m):
        self.mark1=m
class details(student,mark):
    def __init__(self,r,n,c,m,h):
        student.__init__(self,r,n,c)
        mark.__init__(self,m)
        self.hostelflag=h
    def displaydetails(self):
        print("Mark:",self.mark1)
        print("hostelflag:",self.hostelflag)
obj=details(1,"Abhi","MCA",50,True)
obj.display()
obj.displaydetails()
