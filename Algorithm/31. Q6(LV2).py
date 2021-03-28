def sublist_max(profits):

    profit_max = 0
    temp = 0

    for money in profits:
        temp = temp + money if temp + money > 0 else 0
        profit_max = max(profit_max, temp)

    return profit_max

# 테스트
print(sublist_max([7, -3, 4, -8]))
print(sublist_max([-2, -3, 4, -1, -2, 1, 5, -3, -1]))