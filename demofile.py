# demofile.py
f = open("c:\\work\\demo2.txt","wt", encoding="utf-8")
f.write("데이터1번\n데이터2번\n데이터3번\n")
f.close()

#읽기
f = open("c:\\work\\demo2.txt", encoding="utf-8")
print("r---read()---")
result = f.read()
print(result)

print("r---readline()---")
f.seek(0)

print(f.readline(), end="")
print(f.readline(), end="")
print("r---readlines()---")
f.seek(0)
lst = f.readlines()
for item in lst:
    print(item,end="")


f.close() #끝나면 항상 마무리~
