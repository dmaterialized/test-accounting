# a very simple program to demonstrate OOP concepts

class account:
     def __init__(self,filepath):
     # first read the number from the balance file
     with open(filepath,'r') as file:
         self.balance=int(file.read())
        # read the file and store value in "self.balance"

# create vars to store account
account=Account("balance.txt")
