import unittest
import os
import sys
from unittest.mock import patch, Mock

# Intentar import relativo primero, luego absoluto
try:
    from ..src.bank_account import BankAccount
    from ..src.exceptions import WithdrawalTimeRestrictionError
except ImportError:
    # Si falla el import relativo, agregar el directorio padre al path
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from src.bank_account import BankAccount
    from src.exceptions import WithdrawalTimeRestrictionError

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

    @patch('src.bank_account.datetime')
    def test_withdraw(self, mock_datetime):
        # Mock datetime to allow withdrawal (during allowed hours)
        mock_datetime.now.return_value.hour = 10  # 10 AM
        new_balance = self.account.withdraw(300)
        self.assertEqual(new_balance, 700, "Withdrawal did not update the balance correctly")
    
    @patch('src.bank_account.datetime')
    def test_withdraw_insufficient_funds(self, mock_datetime):
        # Mock datetime to allow withdrawal (during allowed hours)
        mock_datetime.now.return_value.hour = 10  # 10 AM
        with self.assertRaises(ValueError):
            self.account.withdraw(1200)  # Try to withdraw more than balance (1000)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    @patch('src.bank_account.datetime')
    def test_withdraw_negative_amount(self, mock_datetime):
        """Test that withdrawing a negative amount raises ValueError"""
        # Mock datetime to allow withdrawal (during allowed hours and weekday)
        mock_datetime.now.return_value.hour = 10  # 10 AM
        mock_datetime.now.return_value.weekday.return_value = 1  # Tuesday
        
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(-100)
        self.assertIn("Withdrawal amount must be positive", str(context.exception))

    @patch('src.bank_account.datetime')
    def test_withdraw_zero_amount(self, mock_datetime):
        """Test that withdrawing zero amount raises ValueError"""
        # Mock datetime to allow withdrawal (during allowed hours and weekday)
        mock_datetime.now.return_value.hour = 10  # 10 AM
        mock_datetime.now.return_value.weekday.return_value = 1  # Tuesday
        
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(0)
        self.assertIn("Withdrawal amount must be positive", str(context.exception))

    def test_transaction_log(self):
        self.account.deposit(200)
        assert os.path.exists('transaction_log.txt')

    def test_count_transaction(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(200)
        assert self._count_lines(self.account.log_file) == 2


    @patch('src.bank_account.datetime')
    def test_withdraw_time_restriction(self, mock_datetime):
        # Test withdrawal outside allowed hours (before 9 AM)
        mock_datetime.now.return_value.hour = 8  # 8 AM (before allowed hours)
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)
        
        # Test withdrawal outside allowed hours (after 5 PM)
        mock_datetime.now.return_value.hour = 18  # 6 PM (after allowed hours)
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)
        
        # Test withdrawal during allowed hours (should work)
        mock_datetime.now.return_value.hour = 10  # 10 AM (allowed hours)
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)  # 1000 - 100 = 900

    @patch('src.bank_account.datetime')
    def test_withdraw_disallow_before_bussiness_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7  # 7 AM (before allowed hours)
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch('src.bank_account.datetime')
    def test_withdraw_disallow_on_saturday(self, mock_datetime):
        # Mock Saturday (weekday() returns 5 for Saturday)
        mock_datetime.now.return_value.weekday.return_value = 5
        mock_datetime.now.return_value.hour = 10  # During business hours but on Saturday
        
        with self.assertRaises(WithdrawalTimeRestrictionError) as context:
            self.account.withdraw(100)
        
        self.assertIn("weekends", str(context.exception))

    @patch('src.bank_account.datetime')
    def test_withdraw_disallow_on_sunday(self, mock_datetime):
        # Mock Sunday (weekday() returns 6 for Sunday)
        mock_datetime.now.return_value.weekday.return_value = 6
        mock_datetime.now.return_value.hour = 10  # During business hours but on Sunday
        
        with self.assertRaises(WithdrawalTimeRestrictionError) as context:
            self.account.withdraw(100)
        
        self.assertIn("weekends", str(context.exception))

    
    def test_deposit_multiple_amounts(self):

        test_casese = [
            {"ammount": 100, "expected": 1100},
            {"ammount": 200, "expected": 1200},
            {"ammount": 300, "expected": 1300},
            {"ammount": 400, "expected": 1400}
        ]
        for case in test_casese:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file='transaction_log.txt')
                new_balance = self.account.deposit(case["ammount"])
                self.assertEqual(new_balance, case["expected"])

