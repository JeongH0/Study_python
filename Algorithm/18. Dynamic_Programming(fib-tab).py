def fib_tab(n):
    fib_list = []

    index = 0
    while n > len(fib_list):
        if index <= 1:
            fib_list.append(1)
        else:
            x = fib_list[index - 2] + fib_list[index - 1]
            fib_list.append(x)
        index += 1

    return fib_list[n - 1]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))