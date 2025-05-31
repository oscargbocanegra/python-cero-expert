import unittest
import sys
import os

# Intentar import relativo primero, luego absoluto
try:
    from .test_bank_account import BankAccountTest
except ImportError:
    # Si falla el import relativo, agregar el directorio padre al path
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from test_bank_account import BankAccountTest

def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTest("test_deposit"))
    suite.addTest(BankAccountTest("test_withdraw"))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())
    
