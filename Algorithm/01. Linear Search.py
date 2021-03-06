# Linear Search
# 리스트의 처음부터 끝까지 순서대로 하나씩 탐색을 진행. -> 리스트 안의 원소의 개수만큼 탐색



def linear_search(element, some_list):
    for i in range(len(some_list)):
        if some_list[i] == element:
            return i
    return None

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))