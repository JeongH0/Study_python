# 높이 n개의 계단을 올라가는 방법을 리턴한다
def staircase(stairs, possible_steps):
    stair_list = [1, 1]

    for i in range(2, stairs + 1):
        count = 0
        for step in possible_steps:
            if i >= step:
                count += stair_list[i - step]
        stair_list.append(count)


    return stair_list[stairs]

print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))