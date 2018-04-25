class Account:
    def __init__(self,file):
        self.file = file
        with open(file,"r") as f:
            self.balance = int(f.read())
            print("Current Balance: ",self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)
        with open(self.file,"w") as f:
            f.write(str(self.balance))


    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)
        with open(self.file,"w") as f:
            f.write(str(self.balance))

class Special_Account(Account):
    def __init__(self, file):
        Account.__init__(self,file)
        self.file = file

    def transfer(self, amount):
        self.balance = self.balance - amount
        print("Current Balance: ", self.balance)
    




