# function2.py
# 스코핑룰(이름 해석 규칙) : LGB 규칙
x = 1 # 전역변수

def func(a):
    return a+x

#호출
print(func(1))

def func2(a):
    x = 5 #지역변수
    return a+x
#호출
print(func2(1))