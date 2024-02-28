def fib(n):
    if n<=1:
        return(n)
    else:
         return (fib(n-1)+fib(n-2))
 
terms=input("Enter the number")    
terms=int(terms)

if(terms<=0):
    print("Enter the positive number")
else:
 
 for z in range(terms):
    print(fib(z))
    
        