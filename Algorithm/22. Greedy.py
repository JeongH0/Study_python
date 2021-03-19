"""
미래를 내다보지 않고, 당장 눈 앞에 보이는 최적의 선택
장점: 구현하기 쉽고, 빠름 / 단점: 최적의 답이 보장되지 않을 수도 있음
언제 최적의 답을 보장해주느냐? -> 최적 부분 구조 / 탐욕적 선택 속성(탐욕스런 선택이 최적의 선택)
탐욕적 선택 속성 = 큰거부터 줘버린다!
"""

def min_coin_count(value, coin_list):
    coin_list.sort()
    coin_list.reverse()

    coin_count = 0

    for coin in coin_list:
        coin_count += value // coin
        value = value % coin

    return coin_count

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))