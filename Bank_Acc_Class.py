class BankAccount:
    def __init__(self,name, acc_number, balance=0.0):

        self.name=name
        self.balance=balance
        self.acc_number=acc_number
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} amount added")
        else:
            print("amount should be more than 0")
    
    def withdraw(self,amount):
        if self.balance >= amount > 0:
            self.balance -= amount
            print(f"{amount} withdraw from your account")
        else:
            print("insufficient balance")
    
    def show_balance(self):
        print(f"{self.balance} is your current balance")

user_account=BankAccount("Piyush sharma", "9929594530", 6000)
user_account.show_balance()
user_account.deposit(2000)
user_account.withdraw(1000)
user_account.show_balance()
