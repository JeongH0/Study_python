# Brute Force = 모든 경우의 수 대입. like 해커의 무차별 대입 공격과 같이 -> 효율적인 것은 아님.

# 왼쪽 리스트와 오른쪽 리스트의 원소의 곱 중 최대값 리턴

def max_product(left_cards, right_cards):
    x = 0
    for i in range(len(left_cards)):
        for j in range(len(right_cards)):
            if left_cards[i] * right_cards[j] > x:
                x = left_cards[i] * right_cards[j]
    return x

print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))