# demoFormat.py

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print ("---rjust---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

print ("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(5))

# 문자열 결합
#url = "httl://www.multicampus.com/?page=" + 1
for i in range(10):
    url = "httl://www.multicampus.com/?page=" + str(i)
    print(url)

#파일쓰기
# \ 하나 일 때를 구분하기 위해 두개..가능하나 r로 넣으면 더 편하지!

#f = open("c:\\work\\dome.txt","wt", encoding="utf-8") 
f = open(r"c:\work\dome.txt","wt", encoding = "utf-8") # r == raw sring notation
f = open("c:\\work\\dome.txt","wt", encoding = "utf-8") 
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일읽기
f = open(r"c:\work\dome.txt","rt", encoding = "utf-8")
result = f.read()
print(result)


f.close()

#서식지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(150000000000))
