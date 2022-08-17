import sys
import time
from ReadMap import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from create_car_and_customer import create_car_and_customer
from analyze import get_car_travel_length, get_customer_travel_time, get_customer_waiting_time
from analyze import get_car_travel_length, get_customer_travel_time_10, get_customer_waiting_time_10
from route_ver1 import *
from check_map_position_info import *

import random


class SubWindow(QDialog):
    def __init__(self, people_num, car_num, map_num):
        super().__init__()
        self.people_num = people_num
        self.car_num = car_num
        self.map_num = map_num

        readmap = Map(map_num)
        # 모든 맵의 state를 이차원 배열로 저장=> state 는 char로 저장!!

        self.map = readmap.getMap()
        # 비활성화된 맵x,y저장
        self.map2 = readmap.getDialbePoint()
        self.place = readmap.getPlace()

        self.car_list, self.customer_list = create_car_and_customer(
            int(self.car_num), int(self.people_num), self.map)

        self.initUI()

    def initUI(self):
        # 맵 설정.
        self.hour = 9
        self.min = 0
        self.second = 0
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]
        self.mindist = 10

        # 고객 리스트에서 고객 번호 초기화
        self.cus_list_num = 0
        # 대기중인 고객 list
        self.wait_cus_list = []
        self.visited = []

        self.setObjectName("Dialog")
        self.resize(1045, 612)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 921, 521))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.plus1)
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.plus2)
        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.plus3)
        self.verticalLayout.addWidget(self.pushButton_3)

        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)

        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)

        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)

        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)

        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)

        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.buttons = {}
        self.create_map()

    # 시간, 고객 번호 초기화
    def reset_data(self):
        self.hour = 9
        self.min = 0
        self.second = 0
        self.cus_list_num = 0
        self.wait_cus_list.clear()
    # 차량 이동거리 초기화

    def reset_car_data(self):
        for i in range(len(self.car_list)):
            self.car_list[i].set_travel_length(0)

# 10회 skip
    def plus3(self):
        scenario_num = 0

        self.reset_data()
        self.reset_car_data()

        for scenario_num in range(10):
            for i in range(28800):
                self.second += 1
                if self.second == 60:
                    self.min += 1
                    self.second = 0
                if self.min == 60:
                    self.hour += 1
                    self.min = 0

                #self.label.setText("시간 : " + repr(self.hour) + ":" + repr(self.min) + ":" + repr(self.second))
                # 고객 위치 표시 함수
                self.set_cus_position(scenario_num)
                # 차량 이동 함수
                self.moving_car(scenario_num)

            self.reset_data()

        # 시간 계산 및 표시
        self.calc_time_10()

# 1회 skip
    def plus2(self):
        scenario_num = 0

        self.reset_data()
        self.reset_car_data()

        for i in range(28800):
            self.second += 1
            if self.second == 60:
                self.min += 1
                self.second = 0
            if self.min == 60:
                self.hour += 1
                self.min = 0

            #self.label.setText("시간 : " + repr(self.hour) + ":" + repr(self.min) + ":" + repr(self.second))
            # 고객 위치 표시 함수
            self.set_cus_position(scenario_num)
            # 차량 이동 함수
            self.moving_car(scenario_num)
            # 시간 계산 및 표시
        self.calc_time(scenario_num)
    # 시간 + 1

    def plus1(self):

        self.second += 1
        if self.second == 60:
            self.min += 1
            self.second = 0
        if self.min == 60:
            self.hour += 1
            self.min = 0
        self.label.setText("시간 : " + repr(self.hour) + ":" +
                           repr(self.min) + ":" + repr(self.second))

        # 고객 위치 표시 함수
        scenario_num = 0
        self.set_cus_position(scenario_num)
        # 차량 이동 함수
        self.moving_car(scenario_num)
        # 시간 계산 및 표시
        self.calc_time(scenario_num)
        print(self.customer_list[0][self.cus_list_num].get_time())

    def find_near_car(self, from_x, from_y):
        min_dist = 3
        carinf = []
        near_car_number_list = []

        # t점의 weight 와 state를 받아온다.
        def getmapinfo(x, y):
            return 1, int(self.map[x][y])

        # 재귀함수, count = weight합   xy = 현재 검색위치.
        def bfs(count, x, y):
            if (count > min_dist):
                return 0
            if self.map[x][y] == "3":
                carinf.append(str(x) + "," + str(y))
                return 1
            # 4방향 탐색. 위 아래 오른쪽 왼쪽
            for i in range(4):
                nx = x + self.dx[i]
                ny = y + self.dy[i]
                # nx,ny가 맵 안에 있고 방문 했던 곳이 아닐 때, 재귀로 방문.
                if nx >= 0 and nx < 15 and ny >= 0 and ny < 20:
                    if self.visited[nx][ny] == False:
                        # 벽일 때, continue
                        if self.map[nx][ny] == "0":
                            continue
                        self.visited[nx][ny] = True
                        if bfs(count + 1, nx, ny):
                            return 1
                        self.visited[nx][ny] = False

        bfs(0, from_x, from_y)
        # 중복제거. set사용
        carinf = list(set(carinf))
        # print(carinf)

        # 가까운 차량 번호 찾기
        if (len(carinf) > 0):
            # 찾은 차량 좌표 리스트에서 첫번째 차량의 번호를 찾음
            position_xy = carinf[0].split(',')
            position_x = int(position_xy[0])
            position_y = int(position_xy[1])
            for i in range(len(self.car_list)):
                if (position_x == self.car_list[i].get_position_x()
                        and position_y == self.car_list[i].get_position_y()
                        and self.car_list[i].get_state() == 1):
                    near_car_number_list.append(self.car_list[i].get_car_num())

            # 리스트인 이유: 같은 위치에 차량 여러대일수있음
            #print("가까운차 번호 리스트 ", near_car_number_list)

            return near_car_number_list
        else:
            dummy = []
            return dummy

    # 차량 위치 설정 함수
    def set_car_position(self):
        # 초기 차량 위치 생성
        for i in range(len(self.car_list)):
            self.car_here(self.car_list[i].get_position_x(), self.car_list[i].get_position_y())

    # 고객 위치 설정 함수
    def set_cus_position(self, scenario_num):
        call_list = []
        # 0번 고객 리스트 ui에 표시
        if self.cus_list_num < int(self.people_num):
            self.a, self.b, self.c = self.customer_list[scenario_num][self.cus_list_num].get_time()
            # customer_list[시나리오][고객 번호]의 시간이 현재 시간과 같을 떄,
            if (self.a == self.hour
                and self.b == self.min
                    and self.c == self.second):
                cus_x, cus_y = self.customer_list[scenario_num][self.cus_list_num].get_start_position(
                )
                # 고객 grid에 표시.
                self.person_here(cus_x, cus_y)
                call_list = self.find_near_car(cus_x, cus_y)
                # 근처 차량 존재2
                if len(call_list) != 0:
                    print("")
                    print("고객 번호", self.cus_list_num)
                    print("호출 시각", self.customer_list[scenario_num][self.cus_list_num].get_time())
                    print("고객 출발", self.customer_list[scenario_num][self.cus_list_num].get_start_position(),
                          "고객 도착", self.customer_list[scenario_num][self.cus_list_num].get_dest_position(
                    ),
                        "차량 위치",  self.car_list[call_list[0]].get_position_x(), self.car_list[call_list[0]].get_position_y())
                    print("가까운 차량 번호 ", call_list[0])

                    route = find_route(self.place, self.car_list[call_list[0]].get_position_x(), self.car_list[call_list[0]].get_position_y(),
                                       cus_x, cus_y)

                    del route[0]
                    # call_list[0] => 제일 가까운 차량 번호
                    self.car_list[call_list[0]].set_route(route)

                    self.car_list[call_list[0]].set_state(2)
                    # 사람 한명만 받도록 설계, 추후 수정 필요.
                    dummy = []
                    dummy.append(self.customer_list[scenario_num][self.cus_list_num].get_cus_num())
                    self.car_list[call_list[0]].set_cus_num_list(dummy)
                # 근처차량 없을 때, 고객 번호를 대기열에 추가.
                elif len(call_list) == 0:
                    self.empty(cus_x, cus_y)
                    self.wait_cus_list.append(self.cus_list_num)
                self.cus_list_num += 1

    # 맵 생성
    def create_map(self):
        temp2 = "border-color: rgb(0, 0, 0); border-width : 1.2px; border-style:inset;"
        for i in range(15):
            v = []
            for j in range(20):
                v.append(False)
                temp1 = ""
                if self.map[i][j] == "0":
                    temp1 = "background-color: rgb(222, 104, 104);"
                else:
                    temp1 = "background-color: rgb(200, 200, 200);"
                self.buttons[(i, j)] = QtWidgets.QLabel('%s' % self.map[i][j])
                self.buttons[(i, j)].setStyleSheet(temp1 + temp2)  # buttons의 색깔을 변환해준다.
                self.gridLayout.addWidget(self.buttons[(i, j)], i, j)
            self.visited.append(v)

        # 초기 차량 위치 표시
        self.set_car_position()

    # 맵 상태 변화
    # 활성화된 지역에 차나 사람이 없는 경우
    def empty(self, x, y):
        self.buttons[(x, y)].setStyleSheet(
            "border-color: rgb(0, 0, 0); border-width : 1.2px; border-style:inset; background-color: rgb(200, 200, 200);")
        self.map[x][y] = "1"
        self.buttons[(x, y)].setText("%d" % 1)

    # 사람이 있을 때
    def person_here(self, x, y):
        self.buttons[(x, y)].setStyleSheet(
            "border-color: rgb(0, 0, 0); border-width : 1.2px; border-style:inset; background-color: rgb(150, 255, 150);")
        self.map[x][y] = "2"
        self.buttons[(x, y)].setText("%d" % 2)

    # 차가 있을 때
    def car_here(self, x, y):
        self.buttons[(x, y)].setStyleSheet(
            "border-color: rgb(0, 0, 0); border-width : 1.2px; border-style:inset; background-color: rgb(255, 255, 0);")
        self.map[x][y] = "3"
        self.buttons[(x, y)].setText("%d" % 3)

    # 사람을 태운 차가 있을 때
    def car_and_person_here(self, x, y):
        self.buttons[(x, y)].setStyleSheet(
            "border-color: rgb(0, 0, 0); border-width : 1.2px; border-style:inset; background-color: rgb(0, 255, 150);")
        self.map[x][y] = "4"
        self.buttons[(x, y)].setText("%d" % 4)

    # 현재까지 서비스를 이용한 사람 및 차량의 이동거리 / 시간을 계산
    def calc_time(self, scenario_num):
        self.label_6.setText("차량 총 이동 거리 : " + repr(get_car_travel_length(self.car_list)))
        self.label_7.setText("고객 평균 대기 시간 : " +
                             repr(get_customer_waiting_time(self.customer_list[scenario_num])))
        self.label_8.setText("고객 평균 이동 시간 : " +
                             repr(get_customer_travel_time(self.customer_list[scenario_num])))

    def calc_time_10(self):

        self.label_9.setText("차량 총 이동 거리 : " + repr(get_car_travel_length(self.car_list)))
        self.label_10.setText(
            "고객 평균 대기 시간 : " + repr(get_customer_waiting_time_10(self.customer_list)))
        self.label_11.setText(
            "고객 평균 이동 시간 : " + repr(get_customer_travel_time_10(self.customer_list)))

    # 움직이는 차량 위치정보 그리드맵에 표시(움직이지 않는 차량 제외)
    def moving_car(self, scenario_num):

        for i in range(len(self.car_list)):
            # 차량이 대기중이 아니고 움직이는 state일 때,
            if self.car_list[i].get_state() != 1:
                self.car_list[i].set_count(self.car_list[i].get_count() + 1)
                # 이동경로 []로 받아옴.
                car_route = self.car_list[i].get_route()
                # 이동경로가 남아 있을 때,
                if len(car_route) != 0:
                    temp_dest = car_route[0].split(',')
                    temp_x = int(temp_dest[0])
                    temp_y = int(temp_dest[1])
                    temp_state = 0
                    pos_x = self.car_list[i].get_position_x()
                    pos_y = self.car_list[i].get_position_y()
                    self.car_list[i].set_position_x(temp_x)
                    self.car_list[i].set_position_y(temp_y)

                    cur_people_num = self.car_list[i]
                    for wait_cus in self.wait_cus_list:
                        # 이동 하기 전, 주변에 대기중인 고객이 있다면
                        if abs(self.customer_list[0][wait_cus].get_start_position()[0]-pos_x) + abs(self.customer_list[0][wait_cus].get_start_position()[1]-pos_y) < 2:
                            # 탑승 하는 사람 수가 조건 충족할 때,
                            if self.customer_list[0][wait_cus].get_people_num() <= self.car_list[i].get_people_num():
                                # 목적지 거리가 근처일 때,
                                if abs(self.customer_list[0][wait_cus].get_dest_position()[0] - self.customer_list[0][self.car_list[i].get_cus_num_list()].get_dest_position()[0]) + abs(self.customer_list[0][wait_cus].get_dest_position()[1] - self.customer_list[0][self.car_list[i].get_cus_num_list()].get_dest_position()[1]) < 3:
                                    # 사람 수 만큼 추가
                                    self.car_list[i].set_people_num(
                                        cur_people_num+self.customer_list[0][wait_cus].get_people_num())
                                    # 차량 route 조정.
                                    temp_state = 1
                                    print("근처 존재")

                    # 움직이기 이전 현재 위치 list참조해서 초기화.
                    if check_map_position_info(pos_x, pos_y, self.car_list, self.customer_list[scenario_num]) == 0:
                        self.empty(pos_x, pos_y)
                    elif check_map_position_info(pos_x, pos_y, self.car_list,
                                                 self.customer_list[scenario_num]) == 1:
                        self.car_here(pos_x, pos_y)
                    elif check_map_position_info(pos_x, pos_y, self.car_list,
                                                 self.customer_list[scenario_num]) == 2:
                        self.person_here(pos_x, pos_y)

                    cus_num_list = self.car_list[i].get_cus_num_list()
                    cus_num = cus_num_list[0]

                    # 차가 고객에게 이동중
                    if self.car_list[i].get_state() == 2:
                        # waiting time cal
                        self.customer_list[scenario_num][cus_num].set_waiting_time(
                            self.customer_list[scenario_num][cus_num].get_waiting_time()
                            + self.car_list[i].get_count())
                        self.car_here(temp_x, temp_y)
                    # 차가 사람을 태우고 이동하는 경우
                    elif self.car_list[i].get_state() == 3:
                        # travel time
                        self.customer_list[scenario_num][cus_num].set_travel_time(
                            self.customer_list[scenario_num][cus_num].get_travel_time()
                            + self.car_list[i].get_count())
                        self.car_and_person_here(temp_x, temp_y)

                    del car_route[0]
                    self.car_list[i].set_route(car_route)
                    # self.car_list[i].set_count(0)
                    self.car_list[i].set_travel_length(self.car_list[i].get_travel_length() + 1)

                else:
                    if self.car_list[i].get_state() == 2:
                        cus_num_list = self.car_list[i].get_cus_num_list()
                        cus_num = cus_num_list[0]
                        start_x = self.car_list[i].get_position_x()
                        start_y = self.car_list[i].get_position_y()
                        dest_x, dest_y = self.customer_list[scenario_num][cus_num].get_dest_position(
                        )
                        new_route = find_route(self.place, start_x, start_y, dest_x, dest_y)
                        del new_route[0]
                        self.car_list[i].set_route(new_route)
                        self.car_list[i].set_state(3)
                        self.customer_list[scenario_num][cus_num].set_state(2)

                    elif self.car_list[i].get_state() == 3:
                        cus_num_list = self.car_list[i].get_cus_num_list()
                        cus_num = cus_num_list.pop(0)
                        dest_x, dest_y = self.customer_list[scenario_num][cus_num].get_dest_position(
                        )
                        self.car_list[i].set_state(1)
                        self.car_here(self.car_list[i].get_position_x(),
                                      self.car_list[i].get_position_y())
                        self.customer_list[scenario_num][cus_num].set_state(3)
                        # print(cus_num, "번 고객 도착 : ", dest_x, dest_y)
                        # print("")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "시간 : 9:0:0"))
        self.label_2.setText(_translate("Dialog", "알고리즘 : 다익스트라&bfs"))
        self.label_3.setText(_translate("Dialog", "사람 수 : " + self.people_num))
        self.label_4.setText(_translate("Dialog", "차량 수 : " + self.car_num))
        self.label_5.setText(_translate("Dialog", "맵 번호 : " + self.map_num))

        self.pushButton.setText(_translate("Dialog", "시간 + 1"))
        self.pushButton_2.setText(_translate("Dialog", "skip"))
        self.pushButton_3.setText(_translate("Dialog", "10 skip"))

        self.label_6.setText(_translate("Dialog", "차량 총 이동 거리 : 0"))
        self.label_7.setText(_translate("Dialog", "고객 평균 대기 시간 : 0"))
        self.label_8.setText(_translate("Dialog", "고객 평균 이동 시간 : 0"))

        self.label_9.setText(_translate("Dialog", "10회 분석 - 차량 총 이동 거리 : 0"))
        self.label_10.setText(_translate("Dialog", "10회 분석 - 고객 평균 대기 시간 : 0"))
        self.label_11.setText(_translate("Dialog", "10회 분석 - 고객 평균 이동 시간 : 0"))

    def showModal(self):
        return super().exec_()
