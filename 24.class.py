class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length*self.breadth


r1=Rectangle(20,30)
print(r1.area())