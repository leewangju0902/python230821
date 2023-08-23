# db1.py
import sqlite3


if False: 
    #메모리에 임시 저장
    con = sqlite3.connect(":memory:")
else: 
    #DB에 임시 저장
    con = sqlite3.connect("c:\\work\\test.db")

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
if False: #한번에 다 보여주기
    for row in cur:
        print(row)

    cur.execute("select * from PhoneBook")
    for row in cur:
        print(row)
else: 
    print("---fetchone()---")
    print(cur.fetchone())

    #너무 많으면 나눠서 빼면됨!!
    print("---fetchmany(2)---")
    print(cur.fetchmany(2))    
    
    print("---fetchall()---")
    print(cur.fetchall())

    #execute를 다시 해야 가져올 수 있음.
    cur.execute("select * from PhoneBook")
    print("---fetchall()---")
    print(cur.fetchall())

#연결닫기
con.close()