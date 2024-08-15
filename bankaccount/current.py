from customer import Customer
from bank_account import BankAccount

customer1 = Customer('Helen Smith', '76 The Warren , Blandings , Sussex', '1976-02-29')
account1 = BankAccount(customer1 , 21457288, 1000)
print(account1.customer.get_age())
print(account1.customer.address)
