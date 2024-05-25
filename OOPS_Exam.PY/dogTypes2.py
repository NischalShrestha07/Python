import re


class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        pass    
    def describe(self):
        return f"{self.name} is {self.age} years old. "
class Dog(Animal):
    def speak(self):
        return "Woof!"        
    def fetch(self):
        return "Fetching the ball."
class Cat(Animal):
    def speak(self):
        return "Meow!!"        
    def scratch(self):
        return "Scratchting the Furniture."    
dog=Dog("Romu",3)        
cat=Cat("Whisky",3)        

print(dog.describe())
print(dog.speak())
print(dog.fetch())
print("")

print(cat.describe())
print(cat.speak())
print(cat.scratch())

