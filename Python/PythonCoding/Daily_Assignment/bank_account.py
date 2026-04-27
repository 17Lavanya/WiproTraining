class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    # Getters
    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    # Setters
    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_account_holder(self, account_holder):
        self.__account_holder = account_holder

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative!")

    # Deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Withdraw
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive.")

    # Display
    def display_account_info(self):
        print("----- Account Information -----")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: {self.__balance}")
        print("-------------------------------")
