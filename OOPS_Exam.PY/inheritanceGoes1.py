class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # def stdInfo(self):
    #     print(f"Hello {self.name}.")

class Student(Person):
    def __init__(self, name, age,studentID):
        super().__init__(name, age)
        self.studentID=studentID

    def displayData(self):
        print(f"Name:{self.name}\nAge:{self.age}\nStudent ID:{self.studentID}")
    
    
    
details=Student("Nischal",21,450585)        
details.displayData()


