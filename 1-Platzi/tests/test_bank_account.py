import unittest
import sys
import os

# Agregar el directorio padre al path para que Python pueda encontrar src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(balance=1000)
        

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(300)
        assert new_balance == 700
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1200)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    

       