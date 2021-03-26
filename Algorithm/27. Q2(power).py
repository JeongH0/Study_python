# 거듭제곱 알고리즘의 시간복잡도를 N이 아닌 lgN 으로 만들기

def power(x, y):
    if y == 0:
        return 1

    half = power(x, y // 2)     # dynamic programming 을 하지 않으면 두번 호출해야 하기 때문에 n번

    if y % 2 == 0:
        return half * half
    else:
        return x * half * half

"""
def power(x, y):
    if y == 1:
        return x  
    if y%2 == 0:
        return power(x*x, y/2)
    else:
        return x * power(x*x, (y-1)/2)
"""


# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))