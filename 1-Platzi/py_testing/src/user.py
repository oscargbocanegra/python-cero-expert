from typing import List
from src.bank_account import BankAccount


class User:
    def __init__(self, name: str, email: str) -> None:
        self.name: str = name
        self.email: str = email
        self.accounts: List[BankAccount] = []

    def add_account(self, account: BankAccount) -> None:
        self.accounts.append(account)

    def get_total_balance(self) -> float:
        return sum(account.get_balance() for account in self.accounts)