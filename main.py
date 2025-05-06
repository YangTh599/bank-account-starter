# Thayer Yang
# 06 MAY 2025
# Three Ways to Modify BankAccount Class Attributes
import person

class BankAccount():

    def __init__(self, person: person.Person, account_id: int, balance: float):
        self.holder = person
        self.acc_id = account_id
        self.bal = round(balance, 2)

    def withdraw(self, amount:float):
        
        amount = round(amount, 2)

        if (amount <= self.bal):
            self.bal -= amount

    def deposit(self, amount:float):
        
        amount = round(amount, 2)

        self.bal += amount

    def transfer_funds(self, otherAcc, amount):
        self.bal -= amount
        otherAcc.bal += amount

    def show_balance(self):

        return f"Current Balance: ${self.bal:.2f}"
    
    def get_account_id(self):
        return f"{self.acc_id}"
    
    def get_info(self):

        return f"Name: {self.holder.get_first_name()} {self.holder.get_last_name()}\nBANK ID: {self.get_account_id()}\n{self.show_balance()}\nAge: {self.holder.age}\nSex: {(self.holder.display_sex())[:1]}\nSNN: ***-**-{self.holder.SSN % 10000}"
    
# SCRIPT BELOW
person1 = person.Person("Thayer", "Yang", 18, True, 123456789)

bank1 = BankAccount(person1, 92260406, 1000)

print(bank1.get_info())
    
# Deposit Trials
print()

print("Deposit $500")
bank1.deposit(500)

print("Deposit $422.22")
bank1.deposit(422.22)

print(f"{person1.first_name}'s {bank1.show_balance()}")

print()
# Withdrawl Trials

print("Withdraw $52")
bank1.withdraw(52)

print("Withdraw $90.21")
bank1.withdraw(90.21)

print(f"{person1.first_name}'s {bank1.show_balance()}")

print()

#FINAL SHOWING

print(bank1.get_info())

print()

# transferring funds

person2 = person.Person("Kamea", "Helmstetter", 16, False, 987654321)
person3 = person.Person("Lucas", "Brinks", 17, True, 678912345)
person4 = person.Person("Joshua", "Phillips", 18, True, 345126897)
bank2 = BankAccount(person2, 55642603, 2000)
bank3 = BankAccount(person3, 80085101, 5000000)
bank4 = BankAccount(person4, 10180085, 1.96)

print(bank2.get_info())

print()

print("Kamea is transferring $20 to Thayer\n")


bank2.transfer_funds(bank1, 20)

print(bank1.get_info())
print()
print(bank2.get_info())
print()
# Lucas gives Josh monz
print(bank3.get_info())
print()
print(bank4.get_info())
print()

print("Lucas gives Josh $5000\n")

bank3.transfer_funds(bank4, 5000)
print(bank3.get_info())
print()
print(bank4.get_info())




