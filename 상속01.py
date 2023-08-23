#부모 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
    def working(self):
        print("작업중")
    def coding(self):
        print("코딩중")


#자식 정의
class Student(Person):

    #Override
    def __init__(self, name, phoneNumber, subject, studentID):
        
        # self.name = name
        # self.phoneNumber = phoneNumber
        # 명시적으로 호출 (예쁨!)
        Person.__init__(self, name, phoneNumber)
        
        self.subject = subject
        self.studentID = studentID

    #Override
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(Subject:{0}, studentID: {1})".format(self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "201234")
# print(p.__dict__)
# print(s.__dict__)

p.printInfo()
s.printInfo()
s.working()
s.coding()

