# function4.py
# lambda 함수
# 일회성으로 사용 할때 사용
# 변수 자체를 직접 불러 오지는 못해서 함수로 만들어야 하나?
def g():
    g = lambda x,y: x*x
    return g
def g2():
    g2 =(lambda x:x*x)(3)
    return g2

