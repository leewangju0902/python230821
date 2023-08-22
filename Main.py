# Main.py
import function1 as f1
import function2 as f2
import function3 as f3
import function4 as f4
import Input1 as in1
import grade as gd
import CPerson as cPs

x = 7
if(x == 1):
    f1.setValue(3)
    rst = f1.swap(3,4)
    for item in rst:
        print(item)
elif(x == 3):
    print(f3.union("HAM","EGG"))
    print(f3.union("HAM","EGG","SPAM"))

elif(x == 4):
    print(f4.g())
    print(f4.gg())

elif(x == 5):
    gd.grade()

elif(x == 6):
    value =5
    while value > 0:
        if value <2:
            print ("break")
            break
        print (value)
        value-=1

elif(x == 7):
    p1 = cPs.Person()
    p1.name = "전우치"
    p1.print()
    
    # Run중에 변수를 추가 할 수 있음!! 
    # 그냥 변수 선언하듯이..
    p1.title= "Title_1"
    print(p1.title)

    p2 = cPs.Person()
    p2.print()

else:
    print(f3.union("HAM","EGG"))



