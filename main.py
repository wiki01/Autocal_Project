import sys
from PyQt5.QtWidgets import (QTextEdit, QInputDialog, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout,
                             QFrame, QLabel, QTableWidget, QPushButton, QMessageBox, QTableWidgetItem,
                             QApplication, QHBoxLayout)
# from PyQt5 import QtCore
# from PyQt5.QtCore import QTimer
# import pyvisa as visa


class Docker(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('We Do Autocal, Freedom is not free')


        self.QV_Left = QVBoxLayout() # 왼쪽 기준기가 들어갈 프레임
        self.QV_Right = QVBoxLayout() # 오른쪽 Dut 가 들어갈 프리임

        self.QV_Mid = QVBoxLayout() # 중앙에 설정하는 내용

        self.QH_Mid_In_Top = QHBoxLayout() # 각종 처리 방식 및 등이 들어갈 예정
        self.QH_Mind_In_Bottom = QHBoxLayout() # 하단에 처리결과를 어떻게 처리할것인지 등의 내용이 들어갈 에정


        self.Frame = QHBoxLayout()
        self.Frame.addLayout(self.QV_Left, 1)
        self.Frame.addLayout(self.QV_Mid, 8)
        self.Frame.addLayout(self.QV_Right, 1)

        self.setLayout(self.Frame)

        self.show()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = Docker()
    sys.exit(app.exec_())