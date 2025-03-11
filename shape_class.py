import math
class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, L, B):
        self.L=L
        self.B=B
    
    def area(self):
        return self.L*self.B
class Cricle(Shape):
    def __init__(self, r):
        self.r=r
    def area(self):
        return math.pi*(self.r**2)
rect=Rectangle(15,20)
print(f"Area of rectangle is={rect.area()}")

cricle=Cricle(5)
print(f"Area of cricle is={cricle.area():2}")
