#function1.py
#함수 정의

def setValue(newValue):
    """이 함수는 정수값을 입력받아서
    정수값 2개를 리턴한다 
    """
    # 지역변수
    x = newValue
    #y = "__" 
    #s ="지역변수 x:",x,y
    print("지역변수 x:", x)
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

