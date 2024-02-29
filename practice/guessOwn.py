import random

def guessNumber():
     secretNumber=random.randint(1,50)
    #  print("The secret number is",secretNumber)     
while True:
        n=int(input("Enter the number"))
        attempt=0
        attempt=attempt+1

       

        if(n==secretNumber):
            print("Comgratulations You Have Guessed Correct Number in "+str(attempt)+" attempts")
            break
        elif(n>secretNumber):
            print("Enter Smaller Number please")   
        else:
            print("Enter Greater Number please")   
           
guessNumber ()  