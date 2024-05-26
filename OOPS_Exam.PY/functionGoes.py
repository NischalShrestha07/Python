# def totalSum(*args):
#     return sum(args)# here sum() is a predefined keyword.

# print("The sum of the numbers is:",totalSum(7,8,4,6,4,45))


class BlackAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount    
        print(f"Deposited {amount}. New balance is{self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Funds.")    
        else:
            self.balance-=amount    
            print(f"Deposited {amount}. New balance is {self.balance}.")        