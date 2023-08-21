# DemoDict.py
colors={"apple":"red", "banana":"Yellow"}
print(colors)
# 입력
colors["kiwi"] = "green"
#검색
print(colors["apple"])

for item in colors.items():
    print(item)

phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print("kim" in phone)
print("kang" in phone)
phone["kang"] = "4444"
print("kang" in phone)

# 참조만 복사
# c#에서 new하고 instance만 받아서 사용하는 것처럼
# 하나만 수정해도 동시 수정되므로 주의가 필요하지만,
# 동일한 기능을 여러개 만들 필요 없으므로 좋지.
# 파이썬은 참조 구조로 되어있음!!  
p = phone

print(p)
print(phone)
print(id(phone), id(p))
print(phone["kim"])

# 원본과 별도의 복사본 생성
import copy
device ={"아이폰":5, "아이패드":10}
# 복사!! 대입하면 참조만 대입되므로 복사해서 사용해야함!!!
device2 = copy.deepcopy(device)
device2["아이폰"] = 0
device2["아이패드"] = 0

for item in device.items():
    print(item)

for item in device.keys():
    print(item)
for item in device.values():
    print(item)


print(device)
print(device2)
