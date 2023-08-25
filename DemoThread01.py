import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Worker(QThread): #Back Ground Thread로..
    def run(self):
        while True:
            print("안녕하세요")
            self.sleep(1)

class Worker2(QThread): #Back Ground Thread로..
    def run(self):
        while True:
            print("WORK2")
            self.sleep(2)

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