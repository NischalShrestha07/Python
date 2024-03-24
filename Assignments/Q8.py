
# WAP TO FIND THE FACTORIAL OF GIVEN NUMBER
# num=int(input("Enter any number: "))
# factorial=1
# for i  in range(1,num+1):
#     factorial=factorial*i

# print(factorial)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial cannot be found for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print(f"Factorial of {num} is {factorial(num)}")
