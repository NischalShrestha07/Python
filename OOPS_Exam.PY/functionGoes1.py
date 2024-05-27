

# def factorial(n):
#     if n==0:
#         return 1
    
#     else:
#         return n*factorial(n-1)    

# number=5
# result=factorial(number)
# print(f"Factorial of the entered number is {result}")


# Palinderome Checker:
def isPalindrome(s):
    s=s.lower()
    return s==s[::-1]

# string="racecar"
string="dad"
if isPalindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
        
        
#Easy FIBBONACCI SERIES generator 
n=5        
first = 0
second = 1
print(first)
print(second)
for x in range(1,n):
    third = first + second
    print(third)
    first,second=second,third
    # 