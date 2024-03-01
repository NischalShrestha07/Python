import random

def guessNumber():
     secretNumber=random.randint(1,50)
     attempt=0
     
    #  print("The secret number is",secretNumber)     
     while True:
            guess=int(input("Enter the number"))
            attempt +=1

       

            if guess == secretNumber:
                print("Congratulations You Have Guessed Correct Number in "+str(attempt)+" attempts")
                break
            elif guess>secretNumber:
                print("Enter Smaller Number please")   
            else:
                print("Enter Greater Number please")   
           
guessNumber ()  