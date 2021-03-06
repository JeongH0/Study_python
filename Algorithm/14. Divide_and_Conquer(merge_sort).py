# merge sort: 정렬되어 있는 각각의 리스트. 여기서 리스트의 최소값들을 비교 -> 비교 후 하나의 리스트의 원소들을 모두 소모했다면
# 더이상 대소비교를 하지 않고 남은 리스트의 원소들을 뒤에다 붙임

def merge(list1, list2):
    if len(list1) == 0 or len(list2) == 0:
        return list1 + list2

    else:
        i = 0
        j = 0
        new_list = []
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                new_list.append(list1[i])
                i += 1
            else:
                new_list.append(list2[j])
                j += 1

        if i == len(list1):
            new_list = new_list + list2[j:]
        else:
            new_list = new_list + list1[i:]

        return new_list

# 합병 정렬
def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        return merge(merge_sort(my_list[:len(my_list) // 2]), merge_sort(my_list[len(my_list) // 2: ]))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
