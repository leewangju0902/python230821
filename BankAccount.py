# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name 
        self.balance = balance 
    def deposit(self, amount):
        self.balance += amount 
    def withdraw(self, amount):
        self.balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.id, \
            self.name, self.balance)

class BankAccount2:
    def __init__(self, id, name, balance):
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
account1.balance = 15000000
print(account1)


account2 = BankAccount2(100, "전우치", 15000)
account2.deposit(5000)
account2.withdraw(3000)

# 작성은 되지만 없는거라서 새로 생성됨.
account2.balance = 15000000 

# 값이 기입되는데??
account2.__balance = 15000000 
print(account2.__balance)

# 기입되지 않은 걸로 출력됨!!!
print(account2)


#이름 변경 (_BankAccount__Balnce)
#백도어(테스트하는 용도)
print(account2._BankAccount2__balance)
