class Transaction:
    def __init__(self, from_account, to_account, amount):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

class Account:
    def __init__(self, account_number, balance, name, age, occupation):
        self.account_number = account_number
        self.balance = balance
        self.name = name
        self.age = age
        self.occupation = occupation
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(Transaction(self.account_number, "Deposit", amount))
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction(self.account_number, "Withdraw", amount))
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def transfer(self, to_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            to_account.balance += amount
            self.transactions.append(Transaction(self.account_number, to_account.account_number, amount))
        else:
            print("Insufficient balance or invalid transfer amount.")

    def get_balance(self):
        return self.balance

    def print_transactions(self):
        for transaction in self.transactions:
            print(f"From: {transaction.from_account}, To: {transaction.to_account}, Amount: {transaction.amount}")

class Bank:
    def __init__(self):
        self.accounts = {}
        self.account_number_generator = 1001

    def create_account(self, initial_balance,name,age,occupation):
        account_number = self.account_number_generator
        self.account_number_generator += 1
        account = Account(account_number, initial_balance, name, age, occupation)
        self.accounts[account_number] = account
        return account

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def display_accounts(self):
        for account_number, account in self.accounts.items():
            print(f"Account Number: {account_number}, Balance: {account.get_balance()}, Name: {account.name}, Age: {account.age}, Occupation: {account.occupation}")




bank = Bank()

account1 = bank.create_account(1000,"andie",10,"student")
account2 = bank.create_account(5000,"Oliver",25,"teacher")



deposit = account1.deposit(100)
# acc = bank.display_accounts()

tras = account1.transfer(account2, 500)
past = account1.print_transactions()
wit = account2.withdraw(100)
bal = account2.get_balance()
transfers = account2.print_transactions()
print(transfers)