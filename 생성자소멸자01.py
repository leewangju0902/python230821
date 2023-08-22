# -*- 생성자와 소멸자 -*-
class MyClass:
    #초기화 메소드
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)

    #소멸자 메소드
    def __del__(self):
        print("Instance is deleted!")

#instance 생성
m = MyClass(5)
#del m # instance를 삭제. 주기적으로 자체처리해서 필요 없음
print("전체코드 종료")