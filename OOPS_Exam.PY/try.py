# animal="Python"
print("Choose any one animal(Eagle,Parrot,Lion,Tiger,Python,Crocodile)")
animal=input("Enter Your Choice:")
if(animal=="Eagle" or animal=="Parrot"):
    print("The animal is a Bird.")
elif(animal=="Lion" or animal=="Tiger"):    
    print("The animal is a Mammal.")
elif(animal=="Python" or animal=="Crococdile"):    
    print("The animal is a Reptiles.")   
else:   
    print("Unknown Class.")
    