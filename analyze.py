def get_customer_waiting_time(customers):

    avg_waiting_time = 0
    count = 0

    for i in range(len(customers)):
        if customers[i].get_state() == 3:
            # if customers[i].get_waiting_time() > 0 :
            avg_waiting_time += customers[i].get_waiting_time()
            count += 1

    if count != 0:
        avg_waiting_time /= count
        return avg_waiting_time
    else:
        return 0


def get_customer_travel_time(customers):

    avg_travel_time = 0
    count = 0

    for i in range(len(customers)):
        if customers[i].get_state() == 3:
            avg_travel_time += customers[i].get_travel_time()
            count += 1

    if count != 0:
        avg_travel_time /= count
        return avg_travel_time
    else:
        return 0


def get_car_travel_length(cars):

    car_travel_length = 0

    for i in range(len(cars)):
        car_travel_length += cars[i].get_travel_length()

    return car_travel_length


####################################
# 10회 계산


def get_customer_waiting_time_10(customers):

    avg_waiting_time_list = []
    avg_waiting_time = 0

    for i in range(10):
        avg_waiting_time_list.append(get_customer_waiting_time(customers[i]))

    for i in range(10):
        avg_waiting_time += avg_waiting_time_list[i]

    avg_waiting_time /= len(avg_waiting_time_list)

    return avg_waiting_time


def get_customer_travel_time_10(customers):

    avg_travel_time_list = []
    avg_travel_time = 0

    for i in range(10):
        avg_travel_time_list.append(get_customer_travel_time(customers[i]))

    for i in range(10):
        avg_travel_time += avg_travel_time_list[i]

    avg_travel_time /= len(avg_travel_time_list)

    return avg_travel_time


# 차의 총 이동거리 사용 예제
# print(get_car_travel_length(cars))

# 고객 평균 대시시간 사용 예제
# customers[2][3].set_waiting_time(450)
# print(get_customer_waiting_time(customers[2]))
