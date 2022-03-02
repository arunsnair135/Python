class house:
    def __init__(self,a,l):
        self.area=a
        self.location=l
    def tax_house(self):
        self.tax= (self.area*5/10)
        if(self.location=="Corporation"):
            self.tax+=500
class flat(house):
    def __init__(self,a,l):
        super().__init__(a,l):
        super().tax_house()
    def tax_flat(self):
        self.tax=self.tax*5/100
    def display(self):
        print("tax:",self.tax)
obj
        

