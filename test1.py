# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from pandas import DataFrame
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import copy


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 맵에 Label을 각 좌표마다 넣어 해당 위치정보를 얻을려면 Text를 split으로 해서 알아야 한다. delemmiter = ','
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 고객 class
class Customer:
    def __init__(self, cus_num, start_x, start_y, dest_x, dest_y, share, people_num, hour, minute, second, state):
        self.cus_num = cus_num
        self.start_x = start_x
        self.start_y = start_y
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.share = share
        self.people_num = people_num
        self.hour = hour
        self.minute = minute
        self.second = second
        self.state = state

    def get_cus_num(self):
        return self.cus_num

    def get_start_position(self):
        return int(float(self.start_x)), int(float(self.start_y))

    def get_dest_position(self):
        return self.dest_x, self.dest_y

    def get_share(self):
        return self.share

    def get_people_num(self):
        return self.people_num

    def get_time(self):
        return self.hour, self.minute, self.second

    def get_state(self):
        return self.state
# 고객 발생 시나리오
def call_scenario(Customer):
    customers = []
    cus_num = 0
    hour = 9
    minute = 0
    second = 0
    state = 0

    # 9시 ~ 5시 랜덤 고객 발생
    for i in range(28800):  # 8시간 = 28800초

        if second == 60:
            minute += 1
            second = 0

        if minute == 60:
            hour += 1
            minute = 0

        if hour == 13:
            hour = 1

        # 9am, 2pm 랜덤 고객 발생
        if (hour == 9 or hour == 2) and (random.randrange(1, 1001) <= 30):
            cus_num += 1
            start_x, start_y, dest_x, dest_y, share, people_num = random_customer()
            customers.append(
                Customer(cus_num, start_x, start_y, dest_x, dest_y, share, people_num, hour, minute, second, state))

        # 10am ~ 1pm, 3pm ~ 5pm 랜덤 고객 발생
        if (hour != 9 and hour != 2) and (random.randrange(1, 1001) <= 10):
            cus_num += 1
            start_x, start_y, dest_x, dest_y, share, people_num = random_customer()
            customers.append(
                Customer(cus_num, start_x, start_y, dest_x, dest_y, share, people_num, hour, minute, second, state))

        second += 1

    # end for

    # 결과 출력

    # 총 8시간 평균 432건
    # 1시간당 평균 36건 / 9시, 2시 시간당 평균 108건
    return customers
place = {}
# 사용자로부터 택시까지의 거리 계산하여 가까운 거리 택시가 사용자로 출발 state 가 3인것만.
def close_car(person,carlist_):
    closest_car = 100000
    start_x = 0
    start_y = 0
    for item in carlist_:
        a1,a2=person.get_start_position()
        #에러 발생
        #how_long,temp_x,temp_y = find_route(repr(item).split(",")[0],repr(item).split(",")[1],a1,a2)

    return start_x,start_y

# 랜덤한 고객 정보 생성
def random_customer():
    start_x = random.randint(1, 13)
    start_y = random.randint(1, 11)
    dest_x = random.randint(1, 13)
    dest_y = random.randint(1, 11)
    share = random.randrange(2)

    # 탑승인원 1명 70% / 2명 20% / 3명 10% 확률로 발생
    temp_people_num = random.randrange(1, 11)
    if temp_people_num <= 7:
        people_num = 1
    elif 8 <= temp_people_num <= 9:
        people_num = 2
    else:
        people_num = 3

    return start_x, start_y, dest_x, dest_y, share, people_num
# 길찾기
def find_route(start_x, start_y, dest_x, dest_y):
    start = repr(start_x) + "," + repr(start_y)
    dest = repr(dest_x) + "," + repr(dest_y)

    # dictionary  위치: 가중치
    # 이 방식은 맵 정보를 다 저장해둘 필요가 있음
    print("1")
    routing = {}
    for position in place.keys():
        routing[position] = {"visited": 0, "route": [], "shortest_dist": 0}

        # 새로운 위치 방문
    print("1")
    def visit_place(visit):
        routing[visit]["visited"] = 1
        for to_go, between_dist in place[visit].items():
            dist = routing[visit]["shortest_dist"] + between_dist
            if (routing[to_go]["shortest_dist"] >= dist) or not routing[to_go]["route"]:
                routing[to_go]["shortest_dist"] = dist
                routing[to_go]["route"] = copy.deepcopy(routing[visit]["route"])
                routing[to_go]["route"].append(visit)

                # 방문과정

    visit_place(start)
    print("1")
    while 1:
        min_dist = max(routing.values(), key=lambda x: x["shortest_dist"])["shortest_dist"]
        to_visit = ""

        # name = key / search = values
        for name, search in routing.items():
            if 0 < search["shortest_dist"] <= min_dist and not search["visited"]:
                min_dist = search["shortest_dist"]
                to_visit = name
        if to_visit == "":
            routing[dest]["route"].append(dest)
            break
        visit_place(to_visit)
    print("1")
    return routing[dest]["shortest_dist"], start_x,start_y
# 이동 가능한 지도 상의 모든 정보를 담는 place 생성
def setPlace(Ui_Dialog):
    place = {}
    for i in range(Ui_Dialog.size):
        for j in range(15):
            str_key1 = str(i) + "," + str(j)
            str_state = Ui_Dialog.buttons[(i, j)].text().strip('()').split(',')
            if int(str_state[1]) == 1:
                place[str_key1] = {}
                for k in range(Ui_Dialog.size):
                    if k == 0:
                        if i - 1 >= 0:
                            str_key2 = str(i - 1) + "," + str(j)
                            str_value = Ui_Dialog.buttons[(i - 1, j)].text().strip('()').split(',')
                            if int(str_value[1]) == 1:
                                place[str_key1][str_key2] = int(str_value[0])
                    elif k == 1:
                        if i + 1 < Ui_Dialog.size:
                            str_key2 = str(i + 1) + "," + str(j)
                            str_value = Ui_Dialog.buttons[(i + 1, j)].text().strip('()').split(',')
                            if int(str_value[1]) == 1:
                                place[str_key1][str_key2] = int(str_value[0])
                    elif k == 2:
                        if j - 1 >= 0:
                            str_key2 = str(i) + "," + str(j - 1)
                            str_value = Ui_Dialog.buttons[(i, j - 1)].text().strip('()').split(',')
                            if int(str_value[1]) == 1:
                                place[str_key1][str_key2] = int(str_value[0])
                    elif k == 3:
                        if j + 1 < Ui_Dialog.size:
                            str_key2 = str(i) + "," + str(j + 1)
                            str_value = Ui_Dialog.buttons[(i, j + 1)].text().strip('()').split(',')
                            if int(str_value[1]) == 1:
                                place[str_key1][str_key2] = int(str_value[0])
    return place
# 데이터 UI QTableView에 표시모델 dataframe -> QTableView
class pandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None
class Ui_Dialog(QDialog):
    def setupUi(self):
        # 맵 크기 설정 및 세팅
        self.size = 15
        self.hour = 9
        self.min = 0
        self.second = 0
        self.personlist = 0  # 사용자가 등록되어 있는 수 count
        self.customer_list = call_scenario(Customer)
        # UI 구성------------------------------------------------------------------------
        Dialog.setObjectName("Dialog")
        Dialog.resize(1401, 555)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1401, 531))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.pushButton.clicked.connect(self.plus1)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.tableView = QtWidgets.QTableView(self.horizontalLayoutWidget)
        self.tableView.setObjectName("tableView")
        # table header구성
        self.df = DataFrame(
            {"고객번호": [], "출발x": [], "출발y": [], "도착x": [], "도착y": [], "합승여부": [], "탑승인원": [], "호출시각": [], "현재상태": []})
        self.model1 = pandasModel(self.df)
        self.tableView.setModel(self.model1)
        header = self.tableView.horizontalHeader()
        # table header width 설정
        for i in range(9):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        # UI 구성------------------------------------------------------------------------

        # buttons은 label들의 list, 위치정보를 텍스트로 담고있다.
        self.buttons = {}
        self.create_map()

    # 지역 비활성화 state = 0
    def deactivate(self, x, y):
        self.buttons[(x, y)].setText("(%d,%d)" % (random.randint(1, 9), 0))
        self.buttons[(x, y)].setStyleSheet(
            "border-color: rgb(0, 0, 0); border-width : 1.2px; border-style:inset;background-color: rgb(222, 104, 104);")
    # 지역에 아무도 없을 때 state = 1
    def empty(self, x, y):
        temp = self.buttons[(x, y)].text().replace("(", "").replace(")", "").split(",")
        self.buttons[(x, y)].setText("(%d,%d)" % (int(temp[0]), 1))
        self.buttons[(x, y)].setStyleSheet(
            "border-color: rgb(0, 0, 0); border-width : 1.2px; border-style:inset;background-color: rgb(200, 200, 200);")
    # 지역에 사람이 있을 때 state = 2
    def person_here(self, x, y):
        self.buttons[(x, y)].setStyleSheet(
            "border-color: rgb(0, 0, 0); border-width : 1.2px; border-style:inset; background-color: rgb(138, 139, 221);")
        temp = self.buttons[(x, y)].text().replace("(", "").replace(")", "").split(",")
        self.buttons[(x, y)].setText("(%d,%d)" % (int(temp[0]), 2))
    # 지역에 자동차 있을 때 state = 3
    def car_here(self, x, y):
        self.buttons[(x, y)].setStyleSheet(
            "border-color: rgb(0, 0, 0); border-width : 1.2px; border-style:inset;background-color: rgb(204, 191, 255);")
        temp = self.buttons[(x, y)].text().replace("(", "").replace(")", "").split(",")
        self.buttons[(x, y)].setText("(%d,%d)" % (int(temp[0]), 3))
    # 지역에 자동차가 사람을 태웠을 때 state = 4
    def carperson_here(self, x, y):
        self.buttons[(x, y)].setStyleSheet(
            "border-color: rgb(0, 0, 0); border-width : 1.2px; border-style:inset;background-color: rgb(164, 139, 255);")
        temp = self.buttons[(x, y)].text().replace("(", "").replace(")", "").split(",")
        self.buttons[(x, y)].setText("(%d,%d)" % (int(temp[0]), 4))
    def create_map(self):
        temp2 = "border-color: rgb(0, 0, 0); border-width : 1.2px; border-style:inset;"
        for i in range(self.size):
            for j in range(self.size):
                a = 1
                temp1 = ""
                if a == 0:
                    temp1 = "background-color: rgb(222, 104, 104);"
                else:
                    a = 1
                    temp1 = "background-color: rgb(200, 200, 200);"
                self.buttons[(i, j)] = QtWidgets.QLabel('(%d,%d)' % (random.randint(1, 9), a))
                self.buttons[(i, j)].setStyleSheet(temp1 + temp2)  # buttons의 색깔을 변환해준다.
                self.gridLayout.addWidget(self.buttons[(i, j)], i, j)
        # 비활성화 위치
        self.deactivate(1, 1)
        self.deactivate(2, 5)
        self.deactivate(4, 5)
        self.deactivate(6, 2)
        self.deactivate(7, 9)

        # 자동차 위치
        self.carlist =[]
        self.carlist.append("2,2")
        self.carlist.append("3,8")
        self.carlist.append("5,4")
        self.car_here(2, 2)
        self.car_here(3, 8)
        self.car_here(5, 4)

        self.movelist = {"car" : {"start": [],"time" : []},"personcar" : [{"start": "","time" : 0}]}
    # 1초씩 버튼누를 때 마다 추가.
    def plus1(self):
        self.second += 1
        if self.second == 60:
            self.min += 1
            self.second = 0
        if self.min == 60:
            self.hour += 1
            self.min = 0
        self.label_2.setText("시간 : " + repr(self.hour) + ":" + repr(self.min) + ":" + repr(self.second))

        self.a, self.b, self.c = self.customer_list[self.personlist].get_time()

        # 시간이 생성되어있던 call list와 같을 때
        if self.a == self.hour and self.b == self.min and self.c == self.second:
            d = self.customer_list[self.personlist]
            e, f = d.get_start_position()
            g, h = d.get_dest_position()
            t1,t2 = close_car(self.customer_list[self.personlist],self.carlist)
            #self.movelist["car"]["start"].append(repr(t1)+","+repr(t2))
            #self.movelist["car"]["time"].append(0)

            # dataframe에 사용자 추가 및 table에 업데이트
            self.df.loc[self.personlist] = [d.get_cus_num(), e, f, g, h, d.get_share(), d.get_people_num(),
                                            repr(self.hour) + ":" + repr(self.min) + ":" + repr(self.second),
                                            d.get_state()]
            self.personlist += 1
            self.model1 = pandasModel(self.df)
            self.tableView.setModel(self.model1)

            # 맵에 사용자 위치 표시
            self.person_here(e, f)
    #plus1할 때, 맵 표시하는 함수
    #def moving(self):
        #for temp_c in self.movelist("car"):

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "자동차수 : 3"))
        self.pushButton.setText(_translate("Dialog", "시간 + 1"))
        self.label_2.setText(_translate("Dialog", "시간 : " + repr(self.hour) + ":" + repr(self.min)))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi()
    place = setPlace(ui)
    #print(place)
    Dialog.show()
    sys.exit(app.exec_())