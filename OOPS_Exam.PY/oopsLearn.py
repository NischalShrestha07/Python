class Factory:
    def __init__(self,BT,tyres,ET):
        self.BT=BT
        self.tyres=tyres
        self.ET=ET
    def hello(self):
        print("Hello there!!")
        
# ferrari is an instance/object and self targets the object(ferrari) to store the locations

ferrari=Factory("covered","4","Cycle")
rickshaw=Factory("covered","3","Cycles")
# print(ferrari)          #gives the locations of object
ferrari.hello()
rickshaw.hello()

print(ferrari.BT)
print(ferrari.tyres)
print(ferrari.ET)
