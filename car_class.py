import random

# 차량 class (택시)


class Car:
    def __init__(self, car_num, position_x, position_y, people_num, state, cus_num_list):
        self.car_num = car_num  # 차량 번호
        self.position_x = position_x  # 차량 위치 x
        self.position_y = position_y  # 차량 위치 y
        self.people_num = people_num  # 차량 탑승 인원 (운전자 제외 최대 4명)
        self.state = state  # 차량 상태  (차량 대기중 : 1 / 고객에게 이동 중 : 2 / 고객 탑승 중 : 3)
        self.cus_num_list = []  # 차량 탑승 고객 번호 리스트
        self.dest_x = -1  # 목적지 위치 x
        self.dest_y = -1  # 목적지 위치 y
        self.route = []
        self.count = 0
        self.travel_length = 0  # 차 이동 길이

    def get_car_num(self):
        return self.car_num

    def get_position_x(self):
        return self.position_x

    def get_position_y(self):
        return self.position_y

    def get_people_num(self):
        return self.people_num

    def get_state(self):
        return self.state

    def get_cus_num_list(self):
        return self.cus_num_list

    def get_dest_x(self):
        return self.dest_x

    def get_dest_y(self):
        return self.dest_y

    def get_route(self):
        return self.route

    def get_count(self):
        return self.count

    def get_travel_length(self):
        return self.travel_length

    # 차량 상태  / 차량 대기중 : 1 / 고객에게 이동 중 : 2 / 고객 탑승 중 : 3
    def set_state(self, state):
        self.state = state

    # 차량에 탑승한 인원
    def set_people_num(self, people_num):
        self.people_num = people_num

    # 차량위치 x
    def set_position_x(self, position_x):
        self.position_x = position_x

    # 차량위치 y
    def set_position_y(self, position_y):
        self.position_y = position_y

    # 차량에 탑승한 고객 정보 / list로 표현(여려명이 탑승한 경우가 있으므로)
    def set_cus_num_list(self, cus_num_list):
        self.cus_num_list = cus_num_list

    # 목적지위치 x
    def set_dest_x(self, dest_x):
        self.dest_x = dest_x

    # 목적지위치 y
    def set_dest_y(self, dest_y):
        self.dest_y = dest_y

    def set_route(self, route):
        self.route = route

    def set_count(self, count):
        self.count = count

    # 차의 총 이동 길이
    def set_travel_length(self, travel_length):
        self.travel_length = travel_length


def create_car_list(total_car_num, map_info):

    cars = []

    map_block_list = []
    print(map_info)
    for x in range(len(map_info)):
        for y in range(len(map_info[0])):
            if(map_info[x][y] == "0"):
                map_block_list.append([x, y])

    # print(map_block_list)

    for car_num in range(total_car_num):
        position_x, position_y, people_num, state, cus_num_list = random_car(map_block_list)
        cars.append(Car(car_num, position_x, position_y, people_num, state, cus_num_list))

    # 결과출력 테스트용 함수
    result_out(cars)

    return cars


# 랜덤한 차량 정보 생성
def random_car(map_block_list):
    position_x = random.randrange(0, 15)
    position_y = random.randrange(0, 20)
    people_num = 0
    state = 1
    cus_num_list = []

    # 맵에 없는 위치에 생성시 재생성(출발지, 도착지 모두 맵에 가능한 곳만 생성)
    check = 0
    while (check == 0):
        temp = 0
        for i in range(len(map_block_list)):
            if ((position_x == map_block_list[i][0]) and (position_y == map_block_list[i][1])):
                temp = 1

        if temp == 1:
            position_x = random.randrange(0, 15)
            position_y = random.randrange(0, 20)

        if temp == 0:
            check = 1

    return position_x, position_y, people_num, state, cus_num_list


# 결과 출력 테스트
def result_out(cars):
    if __name__ == "__main__":
        i = 0
        print("car_num    position_x    position_y    people_num    state    cus_num_list")
        while i < len(cars):
            print('%-11s%-14s%-14s%-14s%-12s%-12s' % (cars[i].get_car_num(),
                                                      cars[i].get_position_x(), cars[i].get_position_y(
            ), cars[i].get_people_num(), cars[i].get_state(),
                cars[i].get_cus_num_list()))
            i += 1


# test

# map_info = [["0","0","0","0","0","0","0","0","0","0"],
#            ["0","0","0","0","0","0","0","0","0","0"],
#            ["0","0","0","0","0","0","0","0","0","0"],
#            ["0","0","0","0","0","0","0","0","0","0"],
#            ["0","0","0","0","0","0","0","0","0","0"],
#            ["0","0","0","0","0","0","0","0","0","0"],
#            ["0","0","0","0","0","0","0","0","0","0"],
#            ["0","0","0","0","0","0","0","0","0","0"],
#            ["0","0","0","0","0","0","0","0","0","0"],
#            ["0","0","0","0","0","0","0","0","0","0"],
#            ["0","0","0","0","0","0","0","0","0","0"]]

#car_list = create_car_list(30, map_info)


# 사용 방법
# 다른 py 파일에서
# from car_class import create_car_list
# create_car_list(30) 과 같이 원하는 차량 수를 입력해준다.
