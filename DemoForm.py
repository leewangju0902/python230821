# DemoForm.py
# DemoForm.ui(화면을 저장) + DemoForm.py(로직을 저장)
import sys
import typing
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget

#디자인 파일을 로딩
form_class= uic.loadUiType("DemoForm.ui")[0] #[0] 슬라이싱

#폼 클래스 정의
class Demoform(QDialog, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번재 폼 데모")

#직접 모듈을 실행 했는지 체크

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Demoform = Demoform()
    Demoform.show()
    app.exec_()
