from tkinter.messagebox import RETRY


class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
         return (self.length*self.width)
    def perimeter(self):
         return (2*(self.length+self.width))



calculate=Rectangle(4,5)
print(f"Length:",calculate.length)
print(f"Width:",calculate.width)

print(f"Area of rectangle is:",calculate.area())
print(f"Perimeter of rectangle is:",calculate.perimeter())