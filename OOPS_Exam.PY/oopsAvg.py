
# # Without proper way Using OOPS:
# class Student:
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name=name
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3
        
# s1=Student("Nischal",98,98,97)                
# print("Hello ",s1.name)        
# sum=s1.marks1+s1.marks2+s1.marks3
# avg=sum/3
# print("The average is:",avg)

#With proper way of OOPs:
class Student1:
    def __init__(self,name,marks):
        self.name =name
        self.marks=marks
        
    def getAvg(self):
            sum=0
            for value in self.marks:
                sum +=value
            print("Hi",self.name,"Your average score is:",sum/3)

s1=Student1("Hulk",[98,75,85])            
s1.getAvg()
