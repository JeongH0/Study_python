"""
n을 1과 2의 합으로만 나타내었을 때 경우의수
ex) 4는 1/1/1/1, 1/1/2, 1/2/1, 2/1/1, 2/2 로 총 5개
"""

def staircase(n):

    # 코드를 작성하세요.
    """
    if n == 1 or n == 0:
        return 1
    else:
        return staircase(n - 1) + staircase(n - 2)
    """
    stair_list = [1, 1]

    for i in range(2, n + 1):
        stair_list.append(stair_list[i - 1] + stair_list[i - 2])

    return stair_list[n]



# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
