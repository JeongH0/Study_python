from math import sqrt

# 두 매장의 직선 거리를 계산
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    min_distance = 1000
    min_coordinate = []
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            cal_distance = distance(coordinates[i], coordinates[j])
            if min_distance > cal_distance:
                min_distance = cal_distance
                min_coordinate = [coordinates[i], coordinates[j]]

    return min_coordinate

test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))