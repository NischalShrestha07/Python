

class BankAccount:
    def __init__(self,accountNo,initialBalance):
        self.__accountNo=accountNo
        self.__balance=initialBalance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount    
        else:
            print("Invalid deposit amount")    

    def withdraw(self,amount):
        # if 0<amount<=self.__balance:
        if amount > 0 and amount <= self.__balance:
            self.__balance-=amount   
        else:
            print("Invalid or Insufficient funds for Withdrawal")        
    
    def getBalance(self):
        return self.__balance        

account=BankAccount("1245FGS",2000)
account.deposit(50)
account.withdraw(500)
print(f"Balance:",account.getBalance())

         
         
        