"""
리스트 안에 합이 15인 두 원소가 있는지 판단하는 함수
"""

def sum_in_list(search_sum, sorted_list):
    start = 0
    end = len(sorted_list) - 1

    while start < end:
        cal = sorted_list[start] + sorted_list[end]

        if cal == search_sum:
            return True
        elif cal < search_sum:
            start += 1
        else:
            end -= 1

    return False
"""
    for element in sorted_list:
        find_element = search_sum - element
        if find_element in sorted_list:
            return True

    return False
"""



print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))