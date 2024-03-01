print("")
print("Menu:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option=int(input("Choose any one option:"))

a=int(input("Choose First Number:"))
b=int(input("Choose Second Number:"))

if(option==1):
    print("The sum of the numbers is:",a+b)

elif(option==2):
    print("The subtraction of the numbers is:",a-b)


elif(option==3):
       print("The multiplication of the numbers is:",a*b)



elif(option==4):
    print("The division of the numbers is:",a/b)
    
else:
    print("You have Entered Invalid Option.")