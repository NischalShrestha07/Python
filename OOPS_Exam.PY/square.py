
# # Square of number: 
# # number=[5,4,6,7,9]
# # square=[x**2 for x in number]
# # print(square)

# Factorial of Number:
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)    
print(factorial(5))        

