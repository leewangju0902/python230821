#전역변수
str = "Not Class Member"

class GString:
    def __init__(self):
        #instance memeber var
        self.str = "" 
    def set(self, msg):
        self.str = msg

    def print(self):        
        #print(str) #bug(모호하여 명시적으로!!)        
        print(self.str)

g = GString()
g.set("First Message")
g.print()
