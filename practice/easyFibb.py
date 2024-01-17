
# def fibb(n):
#     if n<=1:
#         return n
#     else:
#         return (fibb(n-1)+fibb(n-2))


# print(fibb(7))       


def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
 

nterms=input("Enter number")       
nterms =int(nterms)

if nterms<=1:
    print("Enter the positive number")
else:
    for x in range(nterms):
     print(fib(x))
