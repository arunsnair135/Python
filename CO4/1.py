class rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b
	def area(self):
		self.a=self.l*self.b
	
		
obj1=rectangle(int(input("Enter the length of first rectangle ")),int(input("Enter the breadth of first rectangle ")))
obj2=rectangle(int(input("Enter the length of second rectangle ")),int(input("Enter the breadth of second rectangle ")))
obj1.area()
obj2.area()

if(obj1.a>obj2.a):
	print("First rectangle has larger area")
else:
	print("Second rectangle has larger area")
