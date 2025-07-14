"""Method overriding is a powerful feature of object oriented programming
that allows you to redefine a method in a derived class.
"""
class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        return self.x * self.y
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    def area(self):
        return 3.14 * super().area()
rec=Shape(5,6)
print("Area of rectangle : ",rec.area())
cir=Circle(5)
print("Area of circle : ",cir.area())