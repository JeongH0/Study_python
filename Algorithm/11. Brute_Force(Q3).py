def trapping_rain(buildings):
    # 코드를 작성하세요
    water = 0

    for i in range(1, len(buildings) - 1):
        left = max(buildings[:i])
        right = max(buildings[i + 1:])

        if buildings[i] < left and buildings[i] < right:
            water = water + min(left, right) - buildings[i]

    return water


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))