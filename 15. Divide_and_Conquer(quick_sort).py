# 두 요소의 위치를 swap
def swap_elements(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


# queck sort의 partition 함수
def partition(my_list, start, end):
    pivot_index = end
    pivot = my_list[pivot_index]
    big_index = start

    for i in range(start, pivot_index):
        if my_list[i] < pivot:
            swap_elements(my_list, i, big_index)
            big_index += 1
    swap_elements(my_list, big_index, pivot_index)

    return big_index

# 퀵 정렬
def quicksort(my_list, start=0, end=None):
    if end == None:
        end = len(my_list) - 1

    if start >= end:
        return my_list

    pivot = partition(my_list, start, end)
    quicksort(my_list, start, pivot - 1)
    quicksort(my_list, pivot + 1, end)

# 만약 start == end 를 base case로 하면? -> 3 2 1 이라는 리스트를 quick sort 하면 1 2 3이 되고,
# 그것을 다시 quicksort 할시 범위가 0 -1 로 무한루프에 빠져버림

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3)
print(list3)