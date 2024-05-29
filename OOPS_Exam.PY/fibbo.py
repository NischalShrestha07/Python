
number=10
first=0
second=1
print(first)
print(second)
for i in range(1,number):
    third=first+second
    print(third)
    first,second=second,third


def isPalindrome(n):
    n=n.lower()
    if n==n[::-1]:
        print("palindrome")
    else:
        print("No") 
string ="non"           
isPalindrome(string)

# f=open("readme.txt","r")
# print(f.read())

#
try:
    f = open("readme.txt", "r")
    print(f.read())
    f.close()  # Always remember to close the file
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
