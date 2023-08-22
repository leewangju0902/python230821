# DemoLoop.py
print ("---while loop---")
value = 5
while value > 0:
    print (value)
    value-=1

print ("---while loop---break")
value = 5
while value > 0:
    if value < 2:
        print ("break")
        break
    print (value)
    value-=1


print ("---for in loop---")
lst = [100, "사과", 3.14]
for it in lst:
    print(it, type(it))


print ("---for in loop---break")
lst = [1,2,3,4,5,6,7,8,9,10]
for it in lst:
    if it>5:
        break
    print(it, type(it))

print ("---for in loop---continue")
lst = [1,2,3,4,5,6,7,8,9,10]
for it in lst:
    if it % 2 == 0:
        continue
    print(it, type(it))

print ("---range()함수")
print(list(range(10)))
print(list(range(2000,2024)))
print(list(range(1,32)))
for i in range(5):
    print(i)

print("---list  내장(함축)")
lst = list(range(1,11)) # 1~10까지 list
print([i**2 for i in lst if i > 5])
tp = ("apple", "kiwi","orange")
print([len(i) for i in tp])
fruits = {100:"apple", 200:"kiwi"}
print([v.upper() for v in fruits.values()])


