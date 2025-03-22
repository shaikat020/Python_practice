"""Create a Python Account class to represent a bank account with two attributes: balance and account_number, where account_number is a unique string identifying the account. Implement methods to deduct an amount (debit) while ensuring the balance doesn’t fall below zero, and add an amount (credit) to the balance. Provide functionality to print the current balance (print_balance). Additionally, include a transfer method to facilitate the transfer of funds between two accounts, ensuring sufficient funds before completing the transaction. Finally, implement a method called get_account_info to return a formatted string containing the account number and current balance. The transfer method must directly update balances and handle insufficient funds warnings, but do so without overcomplicating the implementation."""
class Account:
    def __init__(self, account_number:str, initial_balance):
        self.account_number = account_number
        self.balance = initial_balance
    def debit(self, value):
        if value > self.balance:
            print("Insufficient balance ")
        else:
            self.balance -= value
            print(f"Debited : {value}, Balance : {self.balance}")
    def credit(self, value):
        self.balance += value
        print(f"Credited : {value}, Balance : {self.balance}")
    
    def print_balance(self):
        print(f"Current balance for Account {self.account_number} : Balance : {self.balance}")
    def transfer(self, value):
        if value > self.balance:
            print("Insufficient balance ")
        else:
            self.balance -= value
            print(f"Transferred : {value}, Balance : {self.balance}")
    def get_account(self):
        return f"Account Number : {self.account_number}, Balance : {self.balance}"

account1= Account("12345675", 100)
account1.print_balance()
account1.debit(500)
account1.credit(200)
account1.transfer(400)
account1.transfer(250)
account1.print_balance()
print(account1.get_account())