import random

# 고객 class


class Customer:
    def __init__(self, cus_num, start_x, start_y, dest_x, dest_y, share, people_num, hour, minute, second, state):
        self.cus_num = cus_num  # 고객 번호
        self.start_x = start_x  # 고객 출발 위치 x
        self.start_y = start_y  # 고객 출발 위치 y
        self.dest_x = dest_x  # 고객 도착 위치 x
        self.dest_y = dest_y  # 고객 도착 위치 y
        self.share = share  # 고객 합승 여부 (0, 1) 0 : 합승불가 1 : 합승 가능
        self.people_num = people_num  # 고객 탑승 인원 (1 ~ 4)
        self.hour = hour  # 호출 시간
        self.minute = minute  # 호출 시간
        self.second = second  # 호출 시간
        self.state = state  # 고객 상태 (차량 대기중 : 1 / 차량 탑승 후 이동 중 : 2 / 도착 완료 : 3)
        self.waiting_time = 0  # 고객 대기 시간 (차량 호출 후 차에 탑승하기까지 시간)
        self.travel_time = 0  # 고객 이동 시간 (차에 타고 있는 시간 / 출발지에서 목적지까지 가는 시간)
        self.car_num = -1  # 고객이 탑승한 차량 번호

    def get_cus_num(self):
        return self.cus_num

    def get_start_position(self):
        return self.start_x, self.start_y

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

    def get_waiting_time(self):
        return self.waiting_time

    def get_car_num(self):
        return self.car_num

    def get_travel_time(self):
        return self.travel_time

    # 고객 생태  / 차량 대기중 : 1 / 차량 탑승 후 이동 중 : 2 / 도착 완료 : 3
    def set_state(self, state):
        self.state = state

    # 고객이 차량 호출 후 탑승까지 기다리는 대기시간
    def set_waiting_time(self, waiting_time):
        self.waiting_time = waiting_time

    # 고객이 차량 탑승 후 출발지에서 목적지까지 가는 시간
    def set_travel_time(self, travel_time):
        self.travel_time = travel_time

    # 고객이 탑승한 차량 번호
    def set_car_num(self, car_num):
        self.car_num = car_num

    # 고객 정렬 후 고객 번호 변경을 위해 필요
    def set_cus_num(self, cus_num):
        self.cus_num = cus_num

    def set_time(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s


# 고객 발생 시나리오
def create_call_scenario(total_cus_num, map_info):

    customers = []
    cus_num = 0
    state = 0

    map_block_list = []

    for x in range(len(map_info)):
        for y in range(len(map_info[0])):
            if(map_info[x][y] == "0"):
                map_block_list.append([x, y])

    # 랜덤 고객 생성
    for i in range(total_cus_num):
        hour = random.randrange(9, 17)
        minute = random.randrange(0, 60)
        second = random.randrange(0, 60)
        start_x, start_y, dest_x, dest_y, share, people_num = random_customer(map_block_list)
        customers.append(Customer(cus_num, start_x, start_y, dest_x, dest_y,
                         share, people_num, hour, minute, second, state))
        cus_num += 1
    # end for

    # 시간 기준으로 고객 정렬
    sorted_cus_list = sorted(customers, key=lambda x: (x.hour, x.minute, x.second))

    # 같은 시각에 호출하는 고객 생성 x
    temp_check = 0
    while(temp_check == 0):
        temp = 0
        for i in range(total_cus_num-1):
            temp_h, temp_m, temp_s = sorted_cus_list[i].get_time()
            h, m, s = sorted_cus_list[i+1].get_time()
            if temp_h == h and temp_m == m and temp_s == s:
                temp = 1
                hour = random.randrange(9, 17)
                minute = random.randrange(0, 60)
                second = random.randrange(0, 60)
                sorted_cus_list[i+1].set_time(hour, minute, second)

        if temp == 0:
            temp_check = 1

    # 시간 기준으로 고객 정렬
    sorted_cus_list = sorted(customers, key=lambda x: (x.hour, x.minute, x.second))

    # 고객 번호 정렬
    for i in range(total_cus_num):
        sorted_cus_list[i].set_cus_num(i)

    # 결과 출력 (테스트 / 확인용)
    result_out(sorted_cus_list)

    return sorted_cus_list


# 랜덤한 고객 정보 생성
def random_customer(map_block_list):
    start_x = random.randrange(0, 15)
    start_y = random.randrange(0, 20)
    dest_x = random.randrange(0, 15)
    dest_y = random.randrange(0, 20)
    share = random.randrange(2)

    check = 0
    while (check == 0):
        temp = 0
        for i in range(len(map_block_list)):
            if ((start_x == map_block_list[i][0]) and (start_y == map_block_list[i][1])):
                temp = 1
            if ((dest_x == map_block_list[i][0]) and (dest_y == map_block_list[i][1])):
                temp = 2
            if ((dest_x == start_x) and (dest_y == start_y)):
                temp = 3

        if temp == 1:
            start_x = random.randrange(0, 15)
            start_y = random.randrange(0, 20)

        if temp == 2:
            dest_x = random.randrange(0, 15)
            dest_y = random.randrange(0, 20)

        if temp == 3:
            dest_x = random.randrange(0, 15)
            dest_y = random.randrange(0, 20)

        if temp == 0:
            check = 1

    # 탑승인원 1명 70% / 2명 20% / 3명 10% 확률로 발생
    temp_people_num = random.randrange(1, 11)
    if temp_people_num <= 7:
        people_num = 1
    elif 8 <= temp_people_num <= 9:
        people_num = 2
    else:
        people_num = 3

    return start_x, start_y, dest_x, dest_y, share, people_num

# 결과 출력


def result_out(customers):
    if __name__ == "__main__":
        i = 0
        print("고객번호    출발지점    도착지점    합승여부    탑승인원    호출시각      현재상태")
        while i < len(customers):
            print('%-12s%-12s%-12s%-12s%-12s%-14s%-12s' % (customers[i].get_cus_num(), customers[i].get_start_position(),
                                                           customers[i].get_dest_position(
            ), customers[i].get_share(),
                customers[i].get_people_num(), customers[i].get_time(), customers[i].get_state()))
            i += 1


# create_call_scenario(400, [[1, 2], [3, 4]])

# ex) 3번 고객의 호출시각
# print(customer_list[2].get_time())
