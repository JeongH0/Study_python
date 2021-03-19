def fib_optimized(n):
    fib_list = [0, 0]

    count = 0
    while n > count:
        if count <= 1:
            fib_list = [1, 1]
        else:
            fib_list[1], fib_list[0] = fib_list[1] + fib_list[0], fib_list[1]
        count += 1

    return fib_list[1]

"""
def fib_optimized(n):
    current = 1
    previous = 0
    
    for i in range(1, n):
        current, previous = current + previous, current
    return current
"""

# 테스트
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
