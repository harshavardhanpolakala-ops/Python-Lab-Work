
class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)


# Main Program
name = input("Enter account holder name: ")
account_number = input("Enter account number: ")

account = BankAccount(name, account_number)

while True:
    print("\n--- BANK ACCOUNT SYSTEM ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print("Thank you for using our bank.")
        break

    else:
        print("Invalid choice.")
