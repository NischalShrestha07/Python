# WAP TO CREATE A TUPLE AND PERFORM THE FOLLOWING METHODS:
# 1. Add items
# 2. len()
# 3. check for item in tuple 
# 4. access items 

myTuple=(1,2,3,4,5)
# tuple cannot be changed but can be concadinate two tuples
newTuple=myTuple+(8,9)
print("New Tuple after adding items:",newTuple)


print("\nLength of Tuple is:",len(myTuple))

itemCheck=3
if itemCheck in myTuple:
    print(f"\n{itemCheck} is present in the tuple.")  
else:
    print(f"\n{itemCheck} is not present in the table.")    

print(f"\nFirst item of the tuple is:{myTuple[0]}")    
print(f"\nLast item of the tuple is:{myTuple[-1]}")    