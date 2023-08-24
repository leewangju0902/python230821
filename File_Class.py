# File class():
class CFile():
    def __init__(self):
        super().__init__()
    def Read(self, dir):
        #파일읽기
        f = open(r"c:\work\dome.txt","rt", encoding = "utf-8")
        result = f.read()
        print(result)
        f.close()
        return result
    def write(self, dir, str):
        f = open(r"c:\work\dome.txt","wt", encoding = "utf-8") # r == raw sring notation
        f = open("c:\\work\\dome.txt","wt", encoding = "utf-8") 
        f.write("첫번째\n두번째\n세번째\n")
        f.close()
        pass

#파일쓰기
# \ 하나 일 때를 구분하기 위해 두개..가능하나 r로 넣으면 더 편하지!

#f = open("c:\\work\\dome.txt","wt", encoding="utf-8") 

#파일읽기
f = open(r"c:\work\dome.txt","rt", encoding = "utf-8")
result = f.read()
print(result)



#서식지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(150000000000))
