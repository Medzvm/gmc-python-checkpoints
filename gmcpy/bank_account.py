class account():
    def __init__(self , account_number , account_balance , account_holder):
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_holder = account_holder

    def deposit(amount):
        account_balance=account_balance+amount
    def withdraw(amount_withdrawn):
        if amount_withdrawn <= account_balance:
            account_balance = account_balance - amount_withdrawn
    def check_balance(account_balance):
       print(account_balance)
    

client1 = account(100,20000,"mourad")
client2 = account(101,20000,"amine")
print(client1.account_balance)
print(client1.check_balance)

