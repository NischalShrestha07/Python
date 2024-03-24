# WAP TO FIND THE LARGEST NUMBERS AMONG THE THREE NUMBERS:


n1=int(input("Enter any First Number: "))
n2=int(input("Enter any Second Number: "))
n3=int(input("Enter any Third Number: "))

if(n1>n2 and n1>n3):
    print("The Largest number is:",n1)
elif(n2>n1 and n2>n3):    
    print("The Largest number is:",n2)
else:
    print("The Largest number is:",n3)
        
    