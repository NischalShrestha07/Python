class Animal:
    def __init__(self,name,age,color):
        self.__name=name
        self.__age=age
        self.__color=color

    def getName(self):
        return self.__name    
    def setName(self,name):
        self.__name=name  
        
    def getColor(self):
        print(self.__color)       
    def setColor(self,color):
        self.__color=color
    
    def getAge(self):
        return self.__age
    def setAge(self,age):
        if age>=0:
            self.__age=age    
        else:
            print("Age must be positive.")    

class Dog(Animal):
    def bark(self):
        return "Woof!!"
class Cat(Animal):
    def meow(self):
        return "Meow!!"        

dog= Dog("Buddy",3,"Brown")
cat= Cat("Whiskers",4,"White")

print("Dogs Details:")
print(dog.getName())
print(dog.getAge())
print(dog.getColor())
print(dog.bark())
print(" ")

print("Cats Details:")
print(cat.getName())
print(cat.getName())
print(cat.getAge())
print(cat.getColor())
print(cat.meow())



