# WAP TO CHECK IF THE STRING IS PALINDROME OR NOT


def checkString(data):
    data=data.lower().replace(" ","")

# checks if the string is equal to its reverse
    return data==data[::-1]


string=input("Enter a string: ")   
if checkString(string):
    print(f" '{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")    