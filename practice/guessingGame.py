limit=200
guess=15
while True:
    n=int(input("Enter any number less than 200:\n"))

    if(n==guess):
        print("Congratulations You Guessed correct number")
        break
    
    elif(n>guess):
        print("Enter the greater number.")
    elif(n<limit ):
        print("Enter smaller number less than 200")
   
    elif(n>limit ):
        print("Enter greater number than",n)
    else:
        print("Enter the positive number")
        
print("Thanks For Playing.")