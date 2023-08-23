# ChatGPT.py

class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name
    
    def paintinfo(self):
        print(f"Person ID: {self.person_id}")
        print(f"이름: {self.name}")


class Manager(Person):
    def __init__(self, person_id, name, skill, role):
        super().__init__(person_id, name)
        self.skill = skill
        self.role = role
    
    def paintinfo(self):
        super().paintinfo()
        print(f"기술: {self.skill}")
        print(f"직책: {self.role}")


class Employee(Person):
    def __init__(self, person_id, name, role):
        super().__init__(person_id, name)
        self.role = role
    
    def paintinfo(self):
        super().paintinfo()
        print(f"직책: {self.role}")


# 예시
person1 = Person(1, "John Doe")
person1.paintinfo()

manager1 = Manager(2, "Jane Smith", "리더십", "시니어 매니저")
manager1.paintinfo()

employee1 = Employee(3, "Alice Johnson", "소프트웨어 개발자")
employee1.paintinfo()

manager2 = Manager(4, "Michael Brown", "문제 해결", "프로젝트 매니저")
manager2.paintinfo()

employee2 = Employee(5, "Emily White", "QA 엔지니어")
employee2.paintinfo()

person2 = Person(6, "David Lee")
person2.paintinfo()

manager3 = Manager(7, "Sarah Green", "커뮤니케이션", "부서장")
manager3.paintinfo()

employee3 = Employee(8, "James Davis", "데이터 애널리스트")
employee3.paintinfo()

manager4 = Manager(9, "Alex Turner", "전략 기획", "팀 리더")
manager4.paintinfo()

employee4 = Employee(10, "Olivia Wilson", "UI/UX 디자이너")
employee4.paintinfo()
