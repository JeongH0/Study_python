"""
(N + 1)의 크기인 리스트에, 1부터 N까지의 임의의 자연수가 요소로 할당되어 있습니다. 그렇다면 어떤 수는 꼭 한 번은 반복됨
O(n) 이상의 공간을 사용할 수 없습니다. 즉 사전이나 리스트와 같이 인풋 리스트의 길이에 비례하는 공간 저장 도구를 사용 X
인풋으로 받는 리스트 some_list의 요소들을 바꾸거나 변형할 수 없습니다.
"""

def find_same_number(some_list, start=1, end=None):
    if end == None:
        end = len(some_list) - 1

    if start == end:
        return start

    mid = (start + end) // 2

    left = 0

    for element in some_list:
        if start <= element and element <= mid:
            left += 1

    if left > mid - start + 1:
        return find_same_number(some_list, start, mid)
    return find_same_number(some_list, mid + 1, end)




# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))