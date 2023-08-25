import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Worker(QThread): #Back Ground Thread로..
    a =0
    def run(self):
        while True:
            a+=1
            print("안녕하세요{0}",a)
            self.msleep(10)

class Worker2(QThread): #Back Ground Thread로..
    a =0
    def run(self):
        while True:
            a+=1
            if(a>10):
                print("안녕하세요{0}",a)
                a=0
            self.msleep(10)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.start()

        self.worker2 = Worker2()
        self.worker2.start()


app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()