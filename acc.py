# a very simple program to demonstrate OOP concepts
# v1.0
# DM Cook

class Account:
    def __init__(self,filepath):
        self.filepath=filepath # instance variable - see line 21
     # first read the number from the balance file
        with open(filepath,'r') as file:
            self.balance=int(file.read())
            # read the file and store value in "self.balance"

    def withdraw(self, amount): # calculate subtraction
        self.balance=self.balance - amount
        # don't use "with open('file')" when you can make a method for commit

    def deposit(self, amount): # calculate the addition
        self.balance=self.balance + amount
        # dont use "with open(filename)"
        # when you can make a method for commit instead

    def commit(self):
        # with open(...)
                                            # can't use filepath as that's only
                                            # in the init method!
                                            # one way would be
                                            # def commit(self,path):
                                            # another way:
                                            # let's do a "instance variable"
                                            # instead, in the init, which
                                            # stores in Self..
                                            # self.filepath=filepath is
                                            # defined in init (line 5)

        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))
            # TODO: this does not actually modify the underlying value correctly.


# fun with inheritance and subclasses:  -------------------------------------------
class Checking(Account): # pass the name of the base class as an arg to the subclass when called
    def __init__(self,filepath):
        Account.__init__(self,filepath)     # inherit everything from Account class
                                            # by calling the init of Account as
                                            # subclass 'Checking' is called

    def transfer(self,amount,fee):
        self.balance=self.balance-amount-fee
                                            # add a fee to the transfer (flat rate)
                                            # it doesn't work until you declare
                                            # an instance variable:
        self.fee=fee                          # self.fee=fee


checking=Checking("accounts/balance.txt")   # not sure why this is needed.
                                            # checking.deposit(10) doesn't work
                                            # because checking has no attribute
                                            # "deposit" at this time.
                                            # This is because inheritance
                                            # isn't working yet.
                                            # change class to Checking(Account)
                                            # which defines the base class for
                                            # inheritance.

# create vars to store the account filepath --------------------------------------------------------
account=Account("accounts/balance.txt")  # var is the result of a class
                                            # for some reason we must declare
                                            # enclosing folder here or it
                                            # won't work.


# =================================
# ========= DEV OPS ===============
# =================================

print("before adjustment:")
print(checking.balance) #dot notation points to the attribute of the object 'account'.
# account.withdraw(100)
# print(account.balance)
# account.commit() # pass this to commit data.
checking.transfer(300,1)
checking.commit()
print("after adjustment:")
print(checking.balance)
                                            # don't put the commit down here
                                            # even though it's tempting.
                                            # commit immediately when change
                                            # is made.
