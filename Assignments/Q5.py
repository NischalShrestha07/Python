# WAP TO READ A NUMBER AND DISPLAY THE CORROSPONDING DAY USING if_elif_else. 


# num = int(input("Enter the number to access the day(1-7):"))
# if(num<1 and num>7):
#     print("Invalid Option! Please choose the number between 1 to 7")
while True:
    # num = int(input("Enter your Choice(1-4): "))
 num = int(input("Enter the number to access the day(1-7):"))
 if num in range(1, 8):
        break 
 else:
    print("Invalid choice. Please enter a number between 1 and 7.")


if(num==1):  
    print("Today is Sunday.")    

elif(num==2):
    print("Today is Monday.")    

elif(num==3):
    print("Today is Tuesday.")    

elif(num==4):
    print("Today is Wednesday.")
    
elif(num==5):
    print("Today is Thrusday.")    

elif(num==6):
    print("Today is Friday.")    

else:
    print("Today is Saturday.")    