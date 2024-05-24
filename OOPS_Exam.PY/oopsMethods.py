class Person:
    name="Nischal"
    occupation="Software Developer"
    networth=10
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=Person()    
a.name="Shubham"
a.occupation="Accountant"
# print(a.name,a.occupation)
a.info()