# Class1.py
class Person:
    """
    인간
    """
    #def __init__(self) -> None:
    def __init__(self): 
        self.name = "default name"
        #pass #없어도 상관없음
    
    def print(self):
        print("My Name is {0}".format(self.name))
        pass

str = "Not Class Member"
class GString:
    def __init__(self):
        self.str = ""
    def set(self, msg):
        self.str = msg
    def __print(self):
        print(str) #global로 땡겨 가는구만.
