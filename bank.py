"""
Create Account class with 2 attributes - balance & account no.
Create methods for debit, credit & printing the balance. (Debit = -value, Credit = +value)
"""
class Account:
    def __init__(self, account_no, initial_balance):
        self.account_no = account_no
        self.balance = initial_balance
    def debit(self, value):
        if value > self.balance :
            print("Insufficient balance")
            
        else:
            
            self.balance -= value
            print(f"Debited : {value}, Balance : {self.balance}")
    def credit(self, value):
        self.balance += value
        print(f"Credited : {value}, Balance : {self.balance}")
        
    def print_balance(self):
        print(f"Account No : {self.account_no}, Balance : {self.balance}")

account1 = Account("123421", 100)
account1.print_balance()
account1.debit(500)
account1.credit(100)
account1.print_balance()


"""فَكَشَفْنَا عَنْكَ غِطَاءَكَ فَبَصَرُكَ الْيَوْمَ حَدِيْدٌ"""
# class Account:  
#     def __init__(self, account_number: str, initial_balance: float = 0.0):  
#         self.account_number = account_number  
#         self.balance = initial_balance  

#     def debit(self, amount: float):  
#         """Deduct an amount from the account balance if sufficient funds are available."""  
#         if amount > self.balance:  
#             print("Insufficient funds for this transaction.")  
#         else:  
#             self.balance -= amount  
#             print(f"Debited {amount:.2f}. New balance: {self.balance:.2f}")  

#     def credit(self, amount: float):  
#         """Add an amount to the account balance."""  
#         self.balance += amount  
#         print(f"Credited {amount:.2f}. New balance: {self.balance:.2f}")  

#     def print_balance(self):  
#         """Print the current account balance."""  
#         print(f"Current balance for account {self.account_number}: {self.balance:.2f}")  

#     def transfer(self, amount: float, target_account):  
#         """Transfer an amount to another account if sufficient funds are available."""  
#         if amount > self.balance:  
#             print("Insufficient funds for transfer.")  
#         else:  
#             self.debit(amount)  
#             target_account.credit(amount)  
#             print(f"Transferred {amount:.2f} to account {target_account.account_number}.")  

#     def get_account_info(self):  
#         """Return a formatted string with the account number and current balance."""  
#         return f"Account Number: {self.account_number}, Current Balance: {self.balance:.2f}"  


# # Example usage:  
# if __name__ == "__main__":  
#     account1 = Account("ACC123", 100.0)  
#     account2 = Account("ACC456", 50.0)  

#     account1.print_balance()  # Current balance for account ACC123: 100.00  
#     account2.print_balance()  # Current balance for account ACC456: 50.00  

#     account1.debit(30)        # Debited 30.00. New balance: 70.00  
#     account1.credit(50)       # Credited 50.00. New balance: 120.00  

#     account1.transfer(70, account2)  # Transferred 70.00 to account ACC456.  
#     account1.print_balance()          # Current balance for account ACC123: 50.00  
#     account2.print_balance()          # Current balance for account ACC456: 120.00  

#     print(account1.get_account_info())  # Account Number: ACC123, Current Balance: 50.00  
#     print(account2.get_account_info())  # Account Number: ACC456, Current Balance: 120.00