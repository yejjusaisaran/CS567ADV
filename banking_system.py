
class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def transfer(self, amount, recipient_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Transfer to {recipient_account.owner}: -${amount:.2f}")
            recipient_account.deposit(amount)
        else:
            print("Invalid transfer amount or insufficient funds.")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history

    def __str__(self):
        return f"Account Number: {self.account_number}, Owner: {self.owner}, Balance: ${self.balance:.2f}"

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, owner):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, owner)
            print("Account created successfully.")
        else:
            print("Account already exists.")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account closed successfully.")
        else:
            print("Account not found.")

def main():
    bank = Bank()

    while True:
        print("\nBanking System Menu")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Show Account Details")
        print("6. Show Transaction History")
        print("7. Close Account")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            owner = input("Enter account owner's name: ")
            bank.create_account(account_number, owner)
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))  
            account = bank.get_account(account_number)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))  
            account = bank.get_account(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == '4':
            source_account_number = input("Enter source account number: ")
            target_account_number = input("Enter target account number: ")
            amount = float(input("Enter amount to transfer: "))  
            source_account = bank.get_account(source_account_number)
            target_account = bank.get_account(target_account_number)
            if source_account and target_account:
                source_account.transfer(amount, target_account)
            else:
                print("One or more accounts not found.")
        elif choice == '5':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print(account)
            else:
                print("Account not found.")
        elif choice == '6':
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                print("Transaction History:")
                for transaction in account.get_transaction_history():
                    print(transaction)
            else:
                print("Account not found.")
        elif choice == '7':
            account_number = input("Enter account number: ")
            bank.close_account(account_number)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
