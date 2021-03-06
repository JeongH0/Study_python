# Divide and Conquer : 재귀적 표현이 들어감. Divide -> Conquer -> Combine 즉, 문제를 나눠서 각각의 문제들을 정복하고, 합침
# 문제가 충분히 작아질때까지 나눠주는 것이 중요. 재귀적 표현에서 Base와 같음

def consecutive_sum(start, end):
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        return consecutive_sum(start, mid) + consecutive_sum(mid + 1, end)


print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))