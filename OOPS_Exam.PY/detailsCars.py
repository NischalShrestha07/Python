
# Question 1
# class Car:
#   def __init__(self,brand,model):
#       self.brand=brand
#       self.model=model
  

# myCar=Car("Bullero","Scorpio")

# print(myCar.brand)
# newCar=Car("Tata","Safari")
# print(newCar.model)


# Question 2
class Car:
  def __init__(self,brand,model):
      self.brand=brand
      self.model=model
  def fullName(self):
      return f"FullName:{self.brand} {self.model}"


myCar=Car("Bullero","Scorpio")
print(myCar.brand)
print(myCar.fullName())

newCar=Car("Tata","Safari")
print(newCar.model)
