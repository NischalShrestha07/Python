class Car:
  def __init__(self,brand,model):
      self.brand=brand
      self.model=model
  def fullName(self):
      return f"FullName:{self.brand} {self.model}"

# Inheritance  Syntax
class ElectricCar(Car):
    def __init__(self, brand, model,batterySize):
        super().__init__(brand, model)
        self.batterySize=batterySize
  
myTesla=ElectricCar("Tesla","Model S","85kWh")  
print(myTesla.fullName())
  
    
myCar=Car("Bullero","Scorpio")
print(myCar.brand)
print(myCar.fullName())

newCar=Car("Tata","Safari")
print(newCar.model)
