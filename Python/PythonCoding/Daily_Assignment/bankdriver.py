from bank_account import BankAccount

print("Bank Account Management System Demo")

# Predefined accounts
account1 = BankAccount("123456", "ABC", 5000)
account2 = BankAccount("789012", "XYZ", 3000)

# Show initial info
account1.display_account_info()
account2.display_account_info()

# Transactions
print("\n--- Transactions ---")

print("\nTransactions for Account 1 (ABC):")
account1.deposit(1500)
account1.withdraw(2000)
account1.withdraw(6000)  # insufficient balance

print("\nTransactions for Account 2 (XYZ):")
account2.deposit(500)
account2.withdraw(1000)


# Final info
print("\n--- Final Account Status ---")
account1.display_account_info()
account2.display_account_info()
