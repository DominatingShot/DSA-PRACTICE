class BankAccount:  
    def __init__(self, account_number, balance):  
        self.account_number = account_number  # Public attribute  
        self.__balance = balance  # Private attribute  
  
    def get_balance(self):  # Getter method  
        return self.__balance  
  
    def set_balance(self, amount):  # Setter method  
        if amount >= 0:  
            self.__balance = amount  
        else:  
            print("Invalid amount! Balance cannot be negative.")  
  
# Creating an account object  
account = BankAccount("123456789", 1000)  
  
# Accessing public member  
print(account.account_number)  # Works fine  
  
# Trying to access private member directly (will raise AttributeError)  
# print(account.__balance)  # Uncommenting this will cause an error  
  
# Using getter method to access private attribute  
print(account.get_balance())  # Works fine  
  
# Using setter method to update private attribute  
account.set_balance(2000)  
print(account.get_balance())  # Updated balance  
  
# Accessing private attribute using name mangling (Not recommended)  
print(account._BankAccount__balance)  # Works, but should be avoided  