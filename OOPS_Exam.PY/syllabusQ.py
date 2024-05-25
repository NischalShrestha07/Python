
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def introduce(self):
        print(f"Hello Namaste 🙏 {self.name}.You are {self.age} years old. Your gender is {self.gender}")    
    def happy_birthday(self):
        self.age+=1    
p1=Person("Nischal",21,"Male")

p1.introduce()

# The number of time we call the "p1.happy_birthday()" method the age of Person will increaseby + 1
# p1.happy_birthday() 
# p1.happy_birthday()
# p1.happy_birthday()
print(p1.age)