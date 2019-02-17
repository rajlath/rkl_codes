from threading import Lock

lock = Lock()


class BankAccount(object):
    def __init__(self):
        self.balance = 0
        self.opened = False

    def get_balance(self):
        if not self.opened:
            raise ValueError("account is not opened.")
        return self.balance

    def open(self):
        if self.opened == True:
            raise ValueError("Account already opened.")
        self.opened = True

    def deposit(self, amount):
        if not self.opened:
            raise ValueError("account is not opened.")
        if amount < 0:
            raise ValueError("Invalid amount")
        with lock:
            self.balance += amount

    def withdraw(self, amount):
        if not self.opened:
            raise ValueError("account is not opened.")
        if amount > self.balance or amount < 0:
            raise ValueError("Invalid amount")
        with lock:
            self.balance -= amount

    def close(self):
        if not self.opened:
            raise ValueError("Account is already closed.")
        self.opened = False
        self.balance= 0