class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        print(f"Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")
            print(f"Current Balance: {self.balance}")

"""obj = ATM(5000)  
obj.deposit(2000)
obj.withdraw(3000)"""
a=int(input("Your initial/last balance : "))
x=int(input("Enter 1 for deposit and 2 for withdraw : "))
obj=ATM(a)
if x==1:
    b=int(input("How much you want to deposit ? "))
    obj.deposit(b)
elif x==2:
    c=int(input("How much you want to withdraw ? "))
    obj.withdraw(c)
else:
    print("Wrong input!")
    
    



