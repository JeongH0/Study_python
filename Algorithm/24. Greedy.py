def min_fee(pages_to_print):
    pages_to_print.sort()

    fee = 0

    for i in range(len(pages_to_print)):
        fee += pages_to_print[i] * (len(pages_to_print) - i)

    return fee


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
