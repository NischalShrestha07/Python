def add(a,b):
    answer=a+b
    print(str(a) + " + " + str(b) + " = " + str(answer)+"\n")

def sub(a,b):
    answer=a-b
    print(str(a) +" - "+ str(b) + " = " + str(answer)+"\n")

def mul(a,b):
    answer=a*b
    print(str(a) +" * "+ str(b)+" = "+str(answer)+"\n")
def div(a,b):
    answer=a/b
    print(str(a) +" / "+ str(b)+" = "+str(answer)+"\n")
while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. MUltiplication")
    print("D. Division")
    print("E. Exit")

    choice =input("Enter Your Choice  ")

    if choice == 'a' or choice == 'A':
        print("Addition")
        a=int(input("Input First Number:"))
        b=int(input("Input Second Number:"))
        add(a,b)
    elif choice == 'b' or choice =='B':
        print("Subtraction")    
        a=int(input("Enter the First Number:"))
        b=int(input("Enter the Second Number:"))
        sub(a,b)
    elif choice == 'c' or choice =='C':
        print("Multiplication")    
        a=int(input("Enter the First Number:"))
        b=int(input("Enter the Second Number:"))
        mul(a,b)

    elif choice == 'd' or choice =='D':
        print("Division")    
        a=int(input("Enter the First Number:"))
        b=int(input("Enter the Second Number:"))
        div(a,b)
    elif choice == "e" or choice == 'E':
        print("Program Ended")    
        quit()



