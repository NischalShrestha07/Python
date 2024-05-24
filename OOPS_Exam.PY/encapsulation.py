class Car:
    totalCar=0

    def __init__(self,brand,model):
        # __brand is made using two "__" which make them private or encapsulated it it from outside the class
        self.brand=brand
        self.model=model
        #   Below code helps to count the numbers of cars.
        Car.totalCar+=1

        #   Getter Initializations:
    def getBrand(self):
            return self.brand+" !"
    def fullName(self):
        return f"FullName:{self.brand} {self.model}"

# Inheritance  Syntax
class ElectricCar(Car):
    def __init__(self, brand, model,batterySize):
        super().__init__(brand, model)
        self.batterySize=batterySize
  
myTesla=ElectricCar("Tesla","Model S","85kWh")  
print(myTesla.fullName())
print(f"Getter Brand: {myTesla.getBrand()}")
  
    
myCar=Car("Bullero","Scorpio")
safari=Car("Tata","Safari")
safari2=Car("Toata","SafariMan")

# print(safari.totalCar)
print(Car.totalCar)

print(myCar.brand)
print(myCar.fullName())

newCar=Car("Tata","Safari")
print(newCar.model)
