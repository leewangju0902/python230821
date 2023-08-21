# DemoStrList.py
# 실행 : ctrl +  f5

strA = "python is very powerful"
strB = "파이썬은 강력해"
strC = """파이썬을
오늘부터
학습니다.
"""

print(strA)
print(len(strB))
print(strC)

result = "py" + "thon"
print(result)

#Slicing, Indexing
print(strA[0])
print(strA[0:6])
print(strA[:6])
print(strA[:])
print(strA[-8:])

print(strB[0])
print(strB[0:6])
print(strB[:6])
print(strB[:])
print(strB[-7:])

print(strC[0])
print(strC[0:6])
print(strC[:6])
print(strC[:])
print(strC[-7:])

print("---List 형식---")
lst = [1,2,3,4,5]
print(len(lst))
print(lst[0])
lst.append(10)
lst.insert(1,20)
print(lst)

colors=["Red","Grn","Blu"]
print(colors)
colors += ["red"]
colors += "red"
print(colors)
colors.remove("red")
print(colors)

colors.sort()
print(colors)
colors.reverse()
print(colors)

for it in colors:
    print(it)


print("---Tuple---")
tp = (10,20,30)
print(len(tp))
print(tp)
print("id:%s, name:%s" % ("Kim","김유신"))

# 함수 정의
def times(a,b):
    return a+b,a*b

# 함수 호출
print(times(5,6))
print(times(5,6)[0])
print(times(5,6)[1])

args = (3,4)
print(times(*args))
print(times(*args)[0])
print(times(*args)[1])

print(times(*args))

print("---형식변환---")
# 중복되는 값을 삭제할 때 Set 로 변환하면 편하넹
# 순서와 관계없이 동일한값을 허용하지 않음
#a = set((1,2,3,4,4,5,5,5,5,5,5,5,6,5))
a = set(("1","2","3","4","5","5"))
print(a)
b = list(a)
b.append(7)
print(b)
c = tuple(b)
print(c)

# Set는 집합과 동일
print("---Set---")
a = {1,2,3,3,3,3,3}
b = {3,4,4,5}
print(len(a))
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#Set는 한개만 출력할 수 없음 List로 변환해서 출력하면 가능
# #print(a[0])
lstA = list(a)
print(lstA[0])



