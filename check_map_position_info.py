# 특정 좌표를 입력하면 해당 좌표에 무엇이 있는지 알려준다.
# 아무것도 없는 경우 0
# 차량이 있는 경우 1
# 고객이 있는 경우 2
# ----------------------------------------------------------
# 사용 방법 ex)
# 다른 py 파일에서
# from check_map_position_info import check_map_position_info
# print(check_map_position_info(3,4, car_list, customer_list))
# ----------------------------------------------------------


# input: 좌표 x , 좌표 y, 차량 리스트, 대기중인 고객 리스트
def check_map_position_info(x, y, car_list, customer_list):
    map_state = 0

    # 검색한 위치에 차량이 있는경우
    for i in range(len(car_list)):
        car_x = car_list[i].get_position_x()
        car_y = car_list[i].get_position_y()

        if ((x == car_x) and (y == car_y)):
            map_state = 1

    # 검색한 위치에 대기중인 고객이 있는 경우
    for i in range(len(customer_list)):
        cus_x, cus_y = customer_list[i].get_start_position()

        if ((x == cus_x) and (y == cus_y)) and customer_list[i].get_state() == 1:
            map_state = 2

    #검색한 위치에 아무것도 없는 경우 : 0 / 차량이 있는 경우 : 1 / 대기중인 고객이 있는 경우 : 2
    return map_state
