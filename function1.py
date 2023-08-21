#function1.py
#함수 정의

def setValue(변수1):
    """지역 변수를 만들고 인자로 값을 대입!
    """
    # 지역변수
    지역변수x = 변수1
    #y = "__" 
    #s ="지역변수 x:",x,y
    print("지역변수 x:", 지역변수x)
    #print(s)

def 셋밸류(변수1):
    """지역 변수를 만들고 인자로 값을 대입!
    """
    # 지역변수
    지역변수x = 변수1
    #y = "__" 
    #s ="지역변수 x:",x,y
    print("지역변수 x:", 지역변수x)
    #print(s)

#함수호출
#result = setValue(5)
#print(result)

#여러개 값을 리턴
def swap(x,y):
    """ 2개의 값을 바꿔서 Return
    """
    return y,x

#호출
#print(swap(3,4))

