class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def findarea(self):
        print(self.length*self.breadth)
    

r1=Rectangle(2,20)
r1.findarea()
