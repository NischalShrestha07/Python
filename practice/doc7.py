# for n in range(2,10):
#     for x in range(2,n):
#         if n%x==0:
#             print(n,"equals",x,"*",n//x)
#             break
#         else:
#             print(n,"is a prime number. ")
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')


for num in range(20,25):
    if num%2==0:
        print("Found the even number",num)
        continue
        # break
    print("Found the odd Number",num)