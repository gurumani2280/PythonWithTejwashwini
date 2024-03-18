#Bank

class Bank :
    def __init__(self,accNo,balance):
        self.__accNo = accNo
        self.__balance = balance
    def displayBalance (self):
        print("Balance",self.__balance)
    def deposit(self,amount):
        self.__balance = self.__balance+amount
        self.displayBalance()

    def withdraw(self,amount):
        if amount <= self.__balance:
            self.__balance -=amount       #self.__balance = self.balance-amount
            self.displayBalance()
        else:
            print("Insufficient Balance")
Cust1 = Bank("001",1000)
Cust1.displayBalance()
Cust1.deposit(2000)
Cust1.withdraw(5000)
Cust1.withdraw(3000)
Cust1.withdraw(500)
