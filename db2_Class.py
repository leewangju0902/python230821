# db1.py
import sys
import sqlite3

class CFile():
    def __init__(self):
        super().__init__()
    def Connect(self):
        if sys.os.path.exist(): 
            # #메모리에 임시 저장
            # con = sqlite3.connect(":memory:")
            #DB에 저장
            con = sqlite3.connect("c:\\work\\ProductList.db")
            #구문 실행은 커서 객체에서
            cur = con.cursor()
        else: 
            con = sqlite3.connect("ProductList.db")
            cur = con.cursor()
            cur.execute(
            "create table Products (id integer primary key autoincrement, Name text, Price integer);")

# if os.path.exists("ProductList.db"):
#     con = sqlite3.connect("ProductList.db")
#     cur = con.cursor()
# else: 



if False: 
    #메모리에 임시 저장
    con = sqlite3.connect(":memory:")
else: 
    #DB에 임시 저장
    con = sqlite3.connect("c:\\work\\sample.db")

#구문 실행은 커서 객체에서
cur = con.cursor()

#테이블 구조 생성(ANSI SQL 92, 99에서 표준)
cur.execute("create table if not exists PhoneBook " +
            " ( id integer primary key autoincrement, name text, phoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values ('홍길동', '010-111');")

#입력 파라미터 처리
name = "전우치"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);",
            (name, phoneNumber))

#다중의 레코드 입력
datalist = (("박문수","010-123"), ("김길동","010-456"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);",
            datalist)

#결과 확인
cur.execute("select * from PhoneBook")
if True: 
    for row in cur:
        print(row)
    #다시 execute해야함!
    cur.execute("select * from PhoneBook")
    for row in cur:
        print(row)
else: 
    print("---fetchall()---")
    print(cur.fetchall())

#커밋을 실행
#닫기전에 커밋을 안하면 저장을 하지 않고 완료됨!!
con.commit()

#연결닫기
con.close()