from car_class import create_car_list
from customer_class import create_call_scenario


# 순서대로 입력 (차량 수 , 고객 수 , 맵 정보)
def create_car_and_customer(total_car_num, total_cus_num, map_info):
    customer_list = []
    car_list = create_car_list(total_car_num, map_info)

    # 각각 다른 고객 시나리오 몇개 생성할 것인지 설정
    for i in range(10):
        customer_list.append(create_call_scenario(total_cus_num, map_info))

    return car_list, customer_list


# 사용 방법
#create_car_and_customer(40, 400, 맵 정보)
