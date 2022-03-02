class student:
    def getdata(self,r,n,c):
        self.roll=r
        self.name=n
        self.course=c
    def display(self):
        print("Roll no:",self.roll)
        print("Name",self.name)
        print("Course",self.course)
class test(student):
    def addmark(self,m):
        self.mark1=m
    def displaymark(self):
        print("Mark 1:",self.mark1)
obj=test()
obj.getdata(1,"Abhi","MCA")
obj.addmark(50)
obj.display()
obj.displaymark()
