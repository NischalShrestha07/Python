# WAP to create menu with following options
#1. add
# 2. sub
# 3. multiply
# 4. division#

print("Choose the option:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
# choice=int(input("Enter your Choice(1-4): "))

while True:
    choice = int(input("Enter your Choice(1-4): "))
    if choice in range(1, 5):
        break 
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

def Addition(num1,num2):
    return num1+num2

def Subtraction(num1,num2):
    return num1-num2

def Multiplication(num1,num2):
    return num1*num2

def Division(num1,num2):
    if num2==0:
        return "Cannot divide by zero"
    else:
        return num1/num2

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

if(choice==1):
    print("The addition of the entered numbers is: ",str(Addition(num1,num2)))
elif(choice==2):
    print("The Subtraction of the entered numbers is: " ,str(Subtraction(num1,num2)))
elif(choice==3):
    print("The Multiplication of the entered numbers is: ",str(Multiplication(num1,num2)))
elif(choice==4):
    print("The Division of the entered numbers is: ",str(Division(num1,num2)))
else:
    print("Invalid Option")  
     
