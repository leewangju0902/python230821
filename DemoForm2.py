# DemoForm.py
# DemoForm.ui(화면을 저장) + DemoForm.py(로직을 저장)
import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget
     
# #웹서버에 통신
# import requests
# #크롤링
# from bs4 import BeautifulSoup

import web2_Class as web2

#디자인 파일을 로딩
form_class= uic.loadUiType("DemoForm2.ui")[0] #[0] 슬라이싱

#폼 클래스 정의
class Demoform(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def firstClick(self):
        self.label.setText("당근 크롤링")
        web = web2.danngn()
        web.Start() 
            

    def secondClick(self):
        self.label.setText("Button 2")
    def thirdClick(self):
        self.label.setText("Button 3")

#직접 모듈을 실행 했는지 체크

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Demoform = Demoform()
    Demoform.show()
    app.exec_()

