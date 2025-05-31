import unittest
import os
import sys

# Intentar import relativo primero, luego absoluto
try:
    from ..src.bank_account import BankAccount
except ImportError:
    # Si falla el import relativo, agregar el directorio padre al path
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(balance=1000, log_file='transaction_log.txt')

    def tearDown(self):
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, file_path):
        if not os.path.exists(file_path):
            return 0
        with open(file_path, 'r') as file:
            return len(file.readlines())
        

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "Deposit did not update the balance correctly")

    def test_withdraw(self):
        new_balance = self.account.withdraw(300)
        self.assertEqual(new_balance, 700, "Withdrawal did not update the balance correctly")
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1200)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_transaction_log(self):
        self.account.deposit(200)
        assert os.path.exists('transaction_log.txt')

    def test_count_transaction(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(200)
        assert self._count_lines(self.account.log_file) == 2

if __name__ == '__main__':
    unittest.main()



