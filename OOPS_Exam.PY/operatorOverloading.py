class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)    
        
    def __mul__(self,scaler):
        return Vector(self.x+scaler.x,self.y+scaler.y)    
    def __repr__(self):
        return f"Vector({self.x},{self.y})"


v1=Vector(2,3)
v2=Vector(4,5)
v3=v1+v2
v4=v1*3
print(v3)
print(v4)
