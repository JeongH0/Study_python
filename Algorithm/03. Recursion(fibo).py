# n번째 피보나치 수

def fib(n):
    if n <= 2:
        return 1

    return fib(n - 2) + fib(n - 1)

for i in range(1, 11):
    print(fib(i))