# WAP TO FIND SUM OF THE NUMBERS FOR THE ELEMENTS OF THE LIST USING reduce()
numbers=[1,2,3,4,5]

sumNumbers=reduce(lambda x,y:x+y,numbers)
print("List of Numbers:",numbers)
print("Sum of the numbers:",sumNumbers)