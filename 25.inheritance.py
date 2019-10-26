class Mammal:
    def walk(self):
        print('i can wak')
        
class Dog(Mammal):
    pass

class Cat(Mammal):
    pass

c=Cat()
c.walk()