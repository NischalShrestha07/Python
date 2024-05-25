n=int(input("Enter number:"))
# below line is direct formula to get the nth value sum. 

# sum=(n*(n-1))/2
sum =0
for i in range (n+1):
    sum=sum+i
print(sum)
