from bank_account import BankAccount
class SavingsAccount(BankAccount):
    """ A class representing a savings account. """
    def __init__(self, customer, account_number, interest_rate, balance = 0):
        """ Initialize the savings account. """
        self.interest_rate = interest_rate
        super().__init__(customer, account_number, balance)
    def  add_interest(self):
        """ Add interest to the account at the rate self.interest_rate. """
        self.balance *= (1. + self.interest_rate/100)

my_savings = SavingsAccount('Matthew Walsh', 41522887, 5.5, 1000)
print(my_savings.check_balance())
my_savings.add_interest()
print(my_savings.check_balance())
