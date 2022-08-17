import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from subwindow import SubWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(300, 300, 614, 300)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 591, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_algorithm = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_algorithm.setObjectName("textEdit_algorithm")
        self.gridLayout.addWidget(self.textEdit_algorithm, 0, 1, 1, 1)
        self.textEdit_people = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_people.setObjectName("textEdit_people")
        self.gridLayout.addWidget(self.textEdit_people, 1, 1, 1, 1)
        self.textEdit_car = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_car.setObjectName("textEdit_car")
        self.gridLayout.addWidget(self.textEdit_car, 2, 1, 1, 1)
        self.textEdit_map = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_map.setObjectName("textEdit_map")
        self.gridLayout.addWidget(self.textEdit_map, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onButtonClicked)
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 614, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.textEdit_map.setPlaceholderText("1")
        self.textEdit_algorithm.setPlaceholderText("1")
        self.textEdit_people.setPlaceholderText("400")
        self.textEdit_car.setPlaceholderText("30")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    # 그리드맵 ui로 전환
    def onButtonClicked(self):
        # 알고리즘 번호 가져오기 1~4번까지
        a = self.textEdit_people.toPlainText()
        b = self.textEdit_car.toPlainText()
        c = self.textEdit_map.toPlainText()
        if self.textEdit_algorithm.toPlainText() == "1":
            win = SubWindow(a, b, c)
            r = win.showModal()
            if r:
                text = win.edit.text()
                self.label.setText(text)
        if self.textEdit_algorithm.toPlainText() == "2":
            print("2")
        if self.textEdit_algorithm.toPlainText() == "3":
            print("3")
        if self.textEdit_algorithm.toPlainText() == "4":
            print("4")

    def show(self):
        super().show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "차량 수"))
        self.label_4.setText(_translate("MainWindow", "맵 번호"))
        self.label.setText(_translate("MainWindow", "알고리즘 번호"))
        self.label_2.setText(_translate("MainWindow", "사람 수"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
