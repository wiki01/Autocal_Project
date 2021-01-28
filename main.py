import sys
from PyQt5.QtWidgets import (QTextEdit, QInputDialog, QWidget, QTabWidget, QVBoxLayout, QHBoxLayout,
                             QFrame, QLabel, QTableWidget, QPushButton, QMessageBox, QTableWidgetItem,
                             QApplication, QHBoxLayout, QDesktopWidget, QListWidget, QComboBox,
                             QSpinBox, QListWidgetItem)


# from PyQt5 import QtCore
# from PyQt5.QtCore import QTimer
# import pyvisa as visa


class Docker(QWidget):
    """
    제일 최상의 윈도우
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle('We Do Autocal, Freedom is not free')

        self.QList_Left = QListWidget()

        Item = QListWidgetItem()
        Load = Module()
        Item.setSizeHint(Load.sizeHint())

        self.QList_Left.addItem(Item)
        self.QList_Left.setItemWidget(Item, Load)

        self.QList_Left.setStyleSheet("border: 1px solid green")
        self.QV_Left = QVBoxLayout()  # 왼쪽 기준기가 들어갈 프레임
        self.QV_Left.addWidget(self.QList_Left)
        # self.QFrame_Left = QFrame()
        # self.QFrame_Left.setLayout(self.QV_Left)

        self.QList_Right = QListWidget()
        self.QList_Right.setStyleSheet("border: 1px solid green")
        self.QV_Right = QVBoxLayout()  # 오른쪽 Dut 가 들어갈 프리임
        self.QV_Right.addWidget(self.QList_Right)
        # self.QFrame_Right = QFrame()
        # self.QFrame_Right.setLayout(self.QV_Right)

        self.QV_Mid = QVBoxLayout()  # 중앙에 설정하는 내용
        self.QFrame_Mid = QFrame()
        self.QFrame_Mid.setLayout(self.QV_Mid)
        self.QFrame_Mid.setStyleSheet("border: 1px solid blue") # 임시 QFrame 디자인 코드
        self.QH_Mid_In_Top = QHBoxLayout()  # 각종 처리 방식 및 등이 들어갈 예정
        self.QH_Mind_In_Bottom = QHBoxLayout()  # 하단에 처리결과를 어떻게 처리할것인지 등의 내용이 들어갈 에정



        self.QH_Parent = QHBoxLayout()
        self.QH_Parent.addLayout(self.QV_Left, 2)
        self.QH_Parent.addWidget(self.QFrame_Mid, 8)
        self.QH_Parent.addLayout(self.QV_Right, 2)

        self.setLayout(self.QH_Parent)

        pos_x = QDesktopWidget().availableGeometry().center().x() - 500
        pos_y = QDesktopWidget().availableGeometry().center().y() - 300
        self.setGeometry(pos_x, pos_y, 1000, 600)  # 중앙으로 이동
        self.setFixedHeight(600)

        self.show()


class Module(QWidget):
    """
    장비의 정보를 담고 있는 모듈
    """
    def __init__(self):
        super().__init__()

        self.QLabel_Model_Name = QLabel(self)
        self.QLabel_Model_Name.setText('모델')
        self.QLable_Image = QLabel(self)
        self.QLable_Image.setText('이미지')
        self.Btn_Setting = QPushButton(self)
        self.Btn_Setting.setText('설정')
        self.QComb_Connect_Type = QComboBox(self)
        self.QSpin_Connect_Number = QSpinBox(self)

        self.QV_Left = QVBoxLayout()
        self.QV_Left.addWidget(self.QLabel_Model_Name, 1)
        self.QV_Left.addWidget(self.QLable_Image, 8)

        self.QV_Right = QVBoxLayout()
        self.QV_Right.addWidget(self.Btn_Setting, 1)
        self.QV_Right.addWidget(self.QComb_Connect_Type, 1)
        self.QV_Right.addWidget(self.QSpin_Connect_Number, 1)
        self.QV_Right.addStretch(7)

        self.Frame = QHBoxLayout()
        self.Frame.addLayout(self.QV_Left, 7)
        self.Frame.addLayout(self.QV_Right, 3)

        self.setLayout(self.Frame)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = Docker()

    sys.exit(app.exec_())
