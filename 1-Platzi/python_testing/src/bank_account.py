from datetime import datetime
from src.exceptions import InsufficientFundsError,WithdrawalTimeRestrictionError

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
        now = datetime.now()
        
        # Check if it's weekend (Saturday = 5, Sunday = 6)
        if now.weekday() in [5, 6]:
            raise WithdrawalTimeRestrictionError("Withdrawals are not allowed on weekends")
        
        # Check business hours (9 AM to 5 PM)
        if now.hour < 9 or now.hour >= 17:
            raise WithdrawalTimeRestrictionError("Withdrawals are only allowed between 9 AM and 5 PM")

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