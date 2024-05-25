# import math

from typing import Self


class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius    
    
    def area(self):
        return 3.14*self.radius*self.radius    


class Square(Shape):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2 
           
class  Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width    

circle=Circle(3)
square=Square(4)
rect=Rectangle(4,4)

# shapes=[Circle(3),Square(4),Circle(2),Rectangle(5,5)]

# If U want multiple area at one without the name
# for shape in shapes:
#     print(f"Area :",shape.area())

print(f"Area of Circle1:{circle.area()}")
print(f"Area of Square:{square.area()}")
print(f"Area of Circle2:{circle.area()}")
print(f"Area of Rectangle:{rect.area()}")
