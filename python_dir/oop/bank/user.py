#!python3


#classes
class BankAccount:
    def __init__(self, int_rate=.0125, balance=500):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $", self.balance)

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance*(1+ self.int_rate)
        return self


class User:

    def __init__(self, name, starting_bal=500):
        self.name = name
        self.balance = starting_bal
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_balance(self):
        print(self.name,": ", self.account.display_balance())

    def transfer(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self, other_user


def main():
    # alex=User("alex")
    # alex.make_deposit(100).make_deposit(200).display_balance()
    #
    # jack=User("jack")
    # jack.make_deposit(300).make_withdrawal(50).make_withdrawal(75).display_balance()
    #
    # jill=User("jill")
    # jill.make_withdrawal(50).make_withdrawal(55).make_withdrawal(30).display_balance()
    #
    # alex.transfer(jill, 100).display_balance()
    # jill.display_balance()

    account_a = BankAccount(.030, 600).deposit(200).deposit(300).withdraw(100).display_account_info()
    account_b = BankAccount().deposit(200).withdraw(100).withdraw(50).withdraw(50).display_account_info()



if __name__ == '__main__':
    main()
