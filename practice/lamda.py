
# # x= lambda a : a+300 
# # print(x(5))

# # x= lambda a,b,c,d,e : a*b+c*d/e 
# # print(x(5,15,1,12,5))

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# p1= Person("Nischal","10000")        
# print(p1.name)
# print(p1.age)

# def EvenOdd(num):
#     if num%2==0:
#         print("Even")
#     else:
#         print("Odd")
# EvenOdd(12)        


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name}({self.age})"
p1=Person("Nischal",25)       
print(p1)
            