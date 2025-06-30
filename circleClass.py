class Circle:
    def __init__(self,radius):
        self.radius=radius
    def circlearea(self):
        pi=3.1416
        a=pi*self.radius*self.radius
        return a
b=Circle(5)
print("Area will be : ",b.circlearea())