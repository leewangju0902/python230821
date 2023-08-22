# Main.py
import Class1 as cCs1

x = 4

if(x == 1):
    p1 = cCs1.Person()
    p1.name = "김"
    p1.print()

elif(x == 2):
    p1 = cCs1.Person()
    p1.name = "김"
    p1.print()
    
    # Run중에 변수를 추가 할 수 있음!! 
    # 임시적으로 저장할 때나 필요
    # 근데 위험하니까 하지말자!!
    p1.title= "Title_1"
    print(p1.title)
    
    #p1에서 변경해도 원본은 바꾸지 않음!
    p2 = cCs1.Person()
    p2.print()

elif(x == 3):
    # Run중에 변수를 추가 할 수 있음!! 
    # 임시적으로 저장할 때나 필요
    # 근데 위험하니까 하지말자!!
    cCs1.Person.title = "New_title"

    p1 = cCs1.Person()
    p2 = cCs1.Person()

    p1.name = "김"
    p2.name = "이"
    
    p1.print()
    p2.print()

    # 따로 저장 가능하다
    # 이럴거면 Class에 만들어서 쓰고 하자!
    # 코드가 너무 지저분해짐!!!!!
    # 왜 이딴걸 만들어 놓은거야..
    p1.title = "타이틀1"
    p1.title = "타이틀2"

    print(p1.title)
    print(p2.title)

elif(x == 4):
    s1 = cCs1.GString()
    g = s1.set("First Message")

    
else:
    print(p1.title)



