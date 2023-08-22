#function5.py
print("---필터링 함수---")
lst=[10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

#필터링하는 함수 정의
print("---일반 함수로 필터링---")
def getBiggerThanY(i)    :
    return i>20
iterL = filter(getBiggerThanY,lst)
for item in iterL:
    print(item)


print("---람다함수 정의---")
iterL = filter(lambda x:x>20,lst)
for item in iterL:
    print(item)
