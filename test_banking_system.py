import unittest
from banking_system import Bank, BankAccount

class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank.create_account('12345', 'John Doe')
        self.bank.create_account('67890', 'Jane Doe')

    def test_create_account(self):
        self.bank.create_account('54321', 'Alice')
        self.assertIsNotNone(self.bank.get_account('54321'))

        self.bank.create_account('12345', 'Bob')
        self.assertIsNone(self.bank.get_account('12345'))

    def test_deposit(self):
        account = self.bank.get_account('12345')
        account.deposit(100)
        self.assertEqual(account.get_balance(), 100)

        account.deposit(-50)
        self.assertEqual(account.get_balance(), 100)

    def test_withdraw(self):
        account = self.bank.get_account('12345')
        account.withdraw(50)
        self.assertEqual(account.get_balance(), 50)

        account.withdraw(100)
        self.assertEqual(account.get_balance(), 50)

    def test_transfer(self):
        source_account = self.bank.get_account('12345')
        target_account = self.bank.get_account('67890')
        source_account.transfer(30, target_account)
        self.assertEqual(source_account.get_balance(), 20)
        self.assertEqual(target_account.get_balance(), 30)

        source_account.transfer(50, target_account)
        self.assertEqual(source_account.get_balance(), 20)
        self.assertEqual(target_account.get_balance(), 30)

    def test_close_account(self):
        self.bank.close_account('12345')
        self.assertIsNone(self.bank.get_account('12345'))

        self.bank.close_account('99999')
        self.assertIsNone(self.bank.get_account('99999'))

if __name__ == '__main__':
    unittest.main()
