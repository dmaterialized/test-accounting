# a very simple program to demonstrate OOP concepts

class Account:
    def __init__(self,filepath):
     # first read the number from the balance file
        with open(filepath,'r') as file:
            self.balance=int(file.read())
            # read the file and store value in "self.balance"

    def withdraw(self, amount):
        # calculate subtraction
        self.balance=self.balance - amount
        # don't use "with open('file')" when you can make a method for commit

    def deposit(self, amount):
        # calculate addition
        self.balance=self.balance + amount


# create vars to store account
account=Account("accounts/balance.txt") #var is the result of a class
# for some reason we must declare enclosing folder here or it won't work.
print(account.balance) #dot notation points to the attribute of the object 'account'.

# ========= DEV OPS ============
account.withdraw(100)
print(account.balance)
# works.
