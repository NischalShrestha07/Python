class FlyAble:
    def fly(self):
        return "The duck is flying."
class Swimmable:
    def swim(self):
        return "The duck is swimming."        

class Duck(FlyAble,Swimmable):
    pass

duck=Duck()        
print(duck.fly())
print(duck.swim())
    