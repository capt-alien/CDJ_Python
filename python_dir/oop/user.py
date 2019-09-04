#!python3


#classes
class User:

    def __init__(self, name, starting_bal=500):
        self.name = name
        self.balance = starting_bal
        # self.password = password

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_balance(self):
        print(self.name,": ", self.balance)
        return self.balance

    def transfer(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.balance += amount



def main():
    alex=User("alex")
    jack=User("jack")
    jill=User("jill")
    alex.make_deposit(100)
    alex.make_deposit(100)
    alex.display_balance()
    jack.make_deposit(300)
    jack.make_withdrawal(50)
    jack.make_withdrawal(75)
    jack.display_balance()
    jill.make_withdrawal(50)
    jill.make_withdrawal(55)
    jill.make_withdrawal(30)
    jill.display_balance()
    alex.transfer(jill, 100)
    alex.display_balance()
    jill.display_balance()



if __name__ == '__main__':
    main()
