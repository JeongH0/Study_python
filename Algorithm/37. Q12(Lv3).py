"""
파라미터 buildings로 [3, 0, 0, 2, 0, 4]가 들어왔다고 합시다. 그러면 0번 인덱스에 높이 33의 건물이, 3번 인덱스에 높이
22의 건물이, 5번 인덱스에 높이 44의 건물이 있다는 뜻
"""
"""
def trapping_rain(buildings):   # Brute Force O(n^2)
    # 코드를 작성하세요
    water = 0

    for i in range(1, len(buildings) - 1):
        left = max(buildings[:i])
        right = max(buildings[i + 1:])

        if buildings[i] < left and buildings[i] < right:
            water = water + min(left, right) - buildings[i]

    return water
"""
def trapping_rain(buildings):   # O(n)
    sum_rain  = 0
    n = len(buildings)

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = buildings[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], buildings[i])

    right_max[n - 1] = buildings[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], buildings[i])

    for i in range(n):
        height = min(left_max[i], right_max[i])
        sum_rain += max(0, height - buildings[i])

    return sum_rain


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))