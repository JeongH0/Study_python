def max_profit(price_list, count):
    earn_max = []

    i = 0
    while i <= count:
        if i <= 1:
            earn_max.append(price_list[i])
        else:
            max_price = 0
            for j in range(1, i // 2 + 1):
                cal_price = earn_max[j] + earn_max[i - j]
                max_price = max(max_price, cal_price)
            if len(price_list) - 1 >= i:
                max_price = max(price_list[i], max_price)
            earn_max.append(max_price)
        i += 1

    return earn_max[count]



# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))
