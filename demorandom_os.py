# demorandom_os.py

import random

print(random.random())
print(random.random())
print(random.uniform(2,5))

print([random.randrange(20) for i in range(10)]) #반복 개수 내 같은 값이 나옴
print([random.randrange(20) for i in range(20)])

print("---샘플링---")
print(random.sample(range(20), 10)) #개수 내 같은 값이 안나옴
print(random.sample(range(20), 10))


from os.path import *
print(abspath("python.exe"))
print(basename("c:\\python310\\python.exe"))

if exists("c:\\python310\\python.exe"):
    print("파일크기 :{0}".format(getsize("c:\\python310\\python.exe")))
else:
    print("파일없음")


from os import * # 운영체제에 관련된 것만 접근
print("운영체제이름 : {0}".format(name))
print("환경변수 : {0}".format(environ))
#system("notepad.exe")
#system("mspaint.exe") #NOTEPAD가 종료되야지 실행됨.

#파일 목록
import glob
result = glob.glob("c:\\work\\*.py")
for item in result:
    print(item)
