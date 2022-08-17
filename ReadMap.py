class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


class Map():
    def __init__(self, map_num):
        self.map = []
        self.disable_point = []
        file = open('./' + map_num + ".txt")
        for x in range(15):
            line = file.readline().replace("n", '').split()
            for y in range(len(line)):
                # 비활성화일때
                if int(line[y]) == 0:
                    # print(int(line[y]))
                    self.disable_point.append(Point(x, y))
            self.map.append(line)

        self.place = {}
        print(self.map)
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                key1 = str(i) + "," + str(j)  # first key
                state = self.map[i][j]
                if int(state) != 0:
                    self.place[key1] = {}
                    for k in range(4):
                        if k == 0:
                            if i-1 >= 0:
                                key2 = str(i-1) + "," + str(j)  # second key
                                next_state = self.map[i-1][j]  # check node's state
                                if next_state != "0":
                                    self.place[key1][key2] = 1
                        elif k == 1:
                            if i+1 < len(self.map):
                                key2 = str(i+1) + "," + str(j)  # second key
                                next_state = self.map[i+1][j]  # check node's state
                                if next_state != "0":
                                    self.place[key1][key2] = 1
                        elif k == 2:
                            if j-1 >= 0:
                                key2 = str(i) + "," + str(j-1)  # second key
                                next_state = self.map[i][j-1]  # check node's state
                                if next_state != "0":
                                    self.place[key1][key2] = 1
                        elif k == 3:
                            if j+1 < len(self.map[i]):
                                key2 = str(i) + "," + str(j+1)  # second key
                                next_state = self.map[i][j+1]  # check node's state
                                if next_state != "0":
                                    self.place[key1][key2] = 1

    def getMap(self):
        return self.map

    # 비활성화 된
    def getDialbePoint(self):
        return self.disable_point

    def getPlace(self):

        return self.place
