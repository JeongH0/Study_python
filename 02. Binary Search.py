# Binary Search
# 정렬이 되어있는 리스트의 중간값과 찾고자 하는 값 비교 -> 탐색범위 절반으로 계속 줄여나감

def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if some_list[mid_index] == element:         # 중간값이 찾고자 하는 값일경우 그 인덱스를 리턴하고 종료
            return mid_index
        elif some_list[mid_index] > element:        # 중간값이 찾고자 하는 값보다 클 경우, 중간값 기준 작은 값들만 다시
            end_index = mid_index - 1
        else:
            start_index = mid_index + 1

    return None             # while문을 빠져나왔을 경우에는 element가 리스트 안에 없다는 것.


print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))