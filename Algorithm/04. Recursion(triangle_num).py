# 1부터 n까지의 합

def triangle_number(n):
    if n == 1:
        return n

    return n + triangle_number(n - 1)

for i in range(1, 11):
    print(triangle_number(i))