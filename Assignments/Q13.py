# WAP TO CREATE DICTIONARY AND APPLY THE FOLLOWING METHODS:
# 1) PRINT THE DICTIONARY ITEMS 
# 2) ACCESS ITEMS
# 3) CHANGE VALUE  
# 4) USE LEN()

myDict={
    "name":"John",
    "age":24,
    "city":"Biratnagar",
    "email":"johnTheLocals123@gmail.com"
}


print("Dictionary Items:")
print(myDict)

print("\nAccessing Items:")
print("Name:",myDict["name"])
print("Age:",myDict["age"])
print("City:",myDict["city"])
print("Email:",myDict["email"])

print("\nChanging Values:")
myDict["age"]=45
print("Updated Age:",myDict["age"])

print("\n Length of Dictionary:",len(myDict))
