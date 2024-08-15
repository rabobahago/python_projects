class BankAccount:
    """ An abstract base class representing a bank account.
    """
    currency = '$'

    def __init__(self, customer, account_number, balance = 0):
        """
        Initialize the BankAccount class with a customer , account number
        and opening balance (which defaults to 0.)
        """
        self.customer = customer
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print('Invalid deposit amount:', amount)
    def withdraw(self, amount):
        if self.balance > 0:
            if amount > self.balance:
                print('Insufficient Fund')
            else:
                self.balance -= amount
        else:
            print('Invalid withdrawal amount:', amount)
    def check_balance(self):
        """ Print a statement of the account balance. """
        print('The balance of your account {:d} is {:s}{:.2f}'.format(self.account_number, self.currency, self.balance))

# my_account = BankAccount('Joe Bloggs', 21457288)
# print(my_account.account_number)
# my_account.deposit(64)
# print(my_account.balance)
