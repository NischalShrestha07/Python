# def calculateGmean(a,b):
#     mean=(a-b)/(a+b)
#     print(mean)
# a=int(input("Enter first number"))    
# b=int(input("Enter second number"))    
# calculateGmean(a,b)
# c=int(input("Enter value of c:"))    
# d=int(input("Enter value of d:"))    


# gmean2=(c+d)/(c+d)
# print(gmean2)

def check(a,b):
    if(a>b):
        print(a, "is greater than",b)
    else:
        print(b, "is greater than",a)


n1=int(input("Enter first number"))    
n2=int(input("Enter second number"))               
print("The greater number among two entered number is:")
check(n1,n2)
