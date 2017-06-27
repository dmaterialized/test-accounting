# a very simple program to demonstrate OOP concepts

class Account:
    def __init__(self,filepath):
        self.filepath=filepath # instance variable - see line 21
     # first read the number from the balance file
        with open(filepath,'r') as file:
            self.balance=int(file.read())
            # read the file and store value in "self.balance"

    def withdraw(self, amount):
        # calculate subtraction
        self.balance=self.balance - amount
        # don't use "with open('file')" when you can make a method for commit

    def deposit(self, amount):
        # calculate the addition
        self.balance=self.balance + amount
        # dont use "with open(filename)" when you can make a method for commit

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


# fun with inheritance and subclasses:  -------------------------------------------
class Checking(Account): # pass the name of the base class as an arg to the subclass when called
    def __init__(self,filepath):
        Account.__init__(self,filepath)     # inherit everything from Account class
                                            # by calling the init of Account whenever
                                            # subclass 'Checking' is called

    def transfer(self,amount):
        self.balance=self.balance-amount

checking=Checking("accounts/balance.txt")   # not sure why this is needed.
                                            # checking.deposit(10) doesn't work
                                            # because checking has no attribute
                                            # "deposit" at this time.
                                            # This is because inheritance
                                            # isn't working yet.
                                            # change class to Checking(Account)
                                            # which defines the base class for
                                            # inheritance.

# create vars to store account --------------------------------------------------------
account=Account("accounts/balance.txt") #var is the result of a class
# for some reason we must declare enclosing folder here or it won't work.

# ========= DEV OPS ============
print(checking.balance) #dot notation points to the attribute of the object 'account'.
print("before adjustment.")

# account.withdraw(100)
# print(account.balance)
# account.commit() # pass this to commit data.
checking.transfer(10)
print("after adjustment:")
print(checking.balance)
account.commit()
