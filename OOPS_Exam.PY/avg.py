num =int(input("How many numbers:"))
total=0

for n in range(num):
    numbers=float(input("Enter any number"))
    total+=numbers
avg=total/num
print("Average of the numbers is:",avg)    