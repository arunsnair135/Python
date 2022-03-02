class student:
    def __init__(self,r,n,c):
        self.roll=r
        self.name=n
        self.course=c
    def display(self):
        print("Roll no:",self.roll)
        print("Name",self.name)
        print("Course",self.course)
class test(student):
    def __init__(self,r,n,c,m):
        super().__init__(r,n,c)
        """student.__init__(self,r,n,c) """
        self.mark1=m
    def displaymark(self):
        print("Mark 1:",self.mark1)
obj=test(1,"Abhi","MCA",50)
obj.display()
obj.displaymark()
