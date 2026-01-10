# class Bank:
#     def __init__(self,name,balance=0):
#         self.name = name
#         self.__balance = balance
#
#     def deposit(self,amount):
#         if amount>0:
#             self.__balance += amount
#             return f'Deposited amount:{amount} and current balance:{self.__balance}'
#         else:
#             return "Invalid amount"
#     def withdraw(self,amount):
#         if amount <=0:
#             return f'Invalid amount'
#         if amount <= self.__balance:
#             self.__balance -= amount
#             return f'Withdrawed amount:{amount} and current balance:{self.__balance}'
#         else:
#             return f'Insufficient funds : curr balance {self.__balance}'
#     @property
#     def getbalance(self):
#         return self.__balance
#
#
# account1 = Bank('john',30000)
# account2 = Bank('sam',0)
#
# print(account1.deposit(2000))
# print(account2.deposit(4500))
# print(account1.withdraw(2000))
# print(account2.withdraw(20000))
# print(account2.getbalance)


class Teacher:
    def __init__(self,name):
        self.name = name

    def welcome(self):
        return f'Welcome , I am {self.name}'

class Student(Teacher):
    def __init__(self,name):
        super().__init__(name)
    def welcome(self):
        return f'Thank you i am a student : {self.name}'


teacher1 = Teacher('alisa')
student1 = Student('John')
print(teacher1.welcome())
print(student1.welcome())

