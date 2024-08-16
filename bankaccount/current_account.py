from bank_account import BankAccount
class CurrentAccount(BankAccount):
    """ A class representing a current (checking) account. """
    def __init__(self, customer, account_number, annual_fee, transaction_limit,  balance=0):
        self.annual = annual_fee
        self.transaction_limit = transaction_limit
        super().__init__(customer, account_number, balance)
    def withdraw(self, amount):
        """
        Withdraw amount if sufficient funds exist in the account and amount
        is less than the single transaction limit.
        """
        if amount < 0:
            print('Invalid withdrawal amount:', amount)
            return
        if amount > self.balance:
            print('Insufficient Fund')
            return
        if amount > self.transaction_limit:
            print('{0:s}{1:.2f} exceeds the single transaction limit of {0:s}{2:.2f}'.format(self.currency , amount , self.transaction_limit))
            return
        self.balance -= amount
    def apply_annual_fee(self):
        """ Deduct the annual fee from the account balance. """
        self.balance = max(0., self.balance - self.annual_fee)


my_current = CurrentAccount('Alison ', 78300991, 20., 200.)
print(my_current.withdraw(220))

my_current.deposit(750)
print(my_current.check_balance())

print(my_current.withdraw(220))
