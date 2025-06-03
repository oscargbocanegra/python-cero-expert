import pytest
from src.bank_account import BankAccount

@pytest.mark.parametrize("ammount, , expected", [
    (100, 1100),
    (200, 1200),
    (300, 1300),
    (400, 1400)
])
def test_deposit_multiple_amounts(ammount, expected):
    
    account = BankAccount(balance=1000, log_file='transaction_log.txt')
    new_balance = account.deposit(ammount)
    assert new_balance == expected


def test_sum():
    a = 4
    b = 5
    assert a + b == 9

