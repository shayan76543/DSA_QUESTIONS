class bank:
    def __init__(self,account_id,account_name):
        self.account_id=account_id
        self.account_name=account_name
        self.balance=0
    def deposit_balance(self,balance):
        self.balance+=balance
        print("Balance Successfully added")
    def cradit_balance(self,balance):
        self.balance-=balance
        if self.insuficient_balance():
            self.balance+=balance
            print("insuficient Balance")
    def display_balance(self):
        print(f"Account_id = {self.account_id}")
        print(f"Account_name = {self.account_name}")
        print(f"Your account Balance is = {self.balance}")
    def insuficient_balance(self):
        if self.balance<0:
            return True
        return False
account1=bank(1,"shayan Ahmad")
account2=bank(2,"sameer Ahmad")
account3=bank(3,"daniyal Ahmad")
account4=bank(4,"Eman Sheikh")
account5=bank(5,"Huria Ahmad")
account6=bank(6,"Sadia Sheikh")
# account1.deposit_balance(10)
# account1.cradit_balance(20)
# account1.display_balance()
# print()
# account2.display_balance()
# print()
# account3.display_balance()
# print()
# account4.display_balance()
# print()
# account5.display_balance()
# print()
# account6.display_balance()
# print()
# account6.cradit_balance(4)
account6.deposit_balance(10)
account6.cradit_balance(4)
account6.display_balance()

