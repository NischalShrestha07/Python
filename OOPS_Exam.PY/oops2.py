class Student:
    collegeName="PUSOE"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("Welcome Student",self.name)    

    def getMarks(self):
        return self.marks
    
#Object Creations: 
s1=Student("Nischal","98")        
s1.welcome()
print(s1.getMarks())

        