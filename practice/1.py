
# # about the input() function
# # message=input("Tell me something about yourself in one word:\n:")
# # print("Explaining Myself in one Word is "+message)


# # age=input("Enter Your Age:")
# # age=int(age)
# # if(age>18):
# #     print("You are capable for voting")
# # else:
# #     print("Sorry, You are not capable for voting")

# prompt="IF You tell Us who You are,We acan Personalize the messages"
# prompt+="\n What is Your First Name:"
# # here (prompt) is a variable not a keyword.

# name=input(prompt)
# print("Hello,"+name)#Concadiantion(+)
# print("Hello,",name)#This runs when the datatypes are same. 

# nischal=1
# while nischal<=10:
#     print(nischal)
#     nischal+=1
''' Write a loop that prompts the user to enter a series of 
pizza toppings until they enter a 'quit' value. As they enter each topping, 
print a message saying you’ll add that topping to their pizza.'''

text="Enter the name of pizza topping you wanted to eat:"
text+="\n Enter 'quit' to end the program: "

message=""
while message != 'quit':
    message=input(text)

    if message !='quit':
        print("\n ThankYou I will Add The",message,"topping")
print("")