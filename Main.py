# Main.py
import function1 as f1
import function2 as f2
import function3 as f3
import function4 as f4
import Input1 as in1

x = 4    
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
else:
    print(f3.union("HAM","EGG"))


