class BankAccount:
    def __init__(self, balance: float = 0.0, log_file: str = None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Account created with initial balance:")
  
    def _log_transaction(self, message: str):
        if self.log_file:
            with open(self.log_file, 'a') as log:
                log.write(f"{message} {self.balance}\n")

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self._log_transaction(f"Deposited: {amount}. New balance:" + str(self.balance))

        return self.balance

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._log_transaction(f"Withdrawn: {amount}. New balance:" + str(self.balance))

        return self.balance

    def get_balance(self) -> float:
        self._log_transaction(f"Current balance: {self.balance}")

        return self.balance