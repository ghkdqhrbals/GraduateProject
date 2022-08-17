import copy

# start_x = 1
# start_y = 1
# dest_x = 2
# dest_y =3

# 길찾기


def find_route(place, start_x, start_y, dest_x, dest_y):
    start = str(start_x) + "," + str(start_y)
    dest = str(dest_x) + "," + str(dest_y)

    # dictionary  위치: 가중치
    # 이 방식은 맵 정보를 다 저장해둘 필요가 있음
    # place = {
    #     "1,1" : {"1,2":5, "2,1":10},
    #     "1,2" : {"1,3":5 ,"2,1":3, "1,1":1},
    #     "1,3" : {"2,3":3 },
    #     "2,1" : {"2,2":9, "1,1":7,},
    #     "2,2" : {"2,3":3, "1,2":4},
    #     "2,3" : {"1,3":11, "2,2":4},
    # }

    routing = {}
    for position in place.keys():
        routing[position] = {"visited": 0, "route": [], "shortest_dist": 0}

    # 새로운 위치 방문
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
    #
    # if __name__ == "__main__":
    #     print("출발지점 : ", start)
    #     print("도착지점 : ", dest)
    #     print("경로 : ", routing[dest]["route"] )
    #     print("소요시간 : ", routing[dest]["shortest_dist"])

    return routing[dest]["route"]
