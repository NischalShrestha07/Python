class Car:
  def __init__(self,brand,model):
      self.brand=brand
      self.model=model
  

myCar=Car("Bullero","Scorpio")

print(myCar.brand)
newCar=Car("Tata","Safari")
print(newCar.model)