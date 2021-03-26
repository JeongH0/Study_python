def sublist_max(profits, start, end):
    if start == end:
        return profits[start]

    mid = (start + end) // 2

    left = sublist_max(profits, start, mid)
    right = sublist_max(profits, mid + 1, end)
    half = half_sum(profits, start, end)

    return max(left, right, half)

def half_sum(profit, start, end):
    mid = (start + end) // 2

    left_sum = 0
    left_max = profit[mid]

    i = mid
    while i >= start:
        left_sum = left_sum + profit[i]
        left_max = max(left_sum, left_max)
        i -= 1

    right_sum = 0
    right_max = profit[mid + 1]

    i = mid + 1
    while i <= end:
        right_sum = right_sum + profit[i]
        right_max = max(right_sum, right_max)
        i += 1

    return left_max + right_max

# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))