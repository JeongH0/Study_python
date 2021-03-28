"""
주식을 딱 한 번 사고 팔았다면 최대 얼마의 수익이 가능?
"""
def max_profit(stock_list):
    # 코드를 작성하세요.
    buy = stock_list[0]
    sell = stock_list[1]
    profit = sell - buy


    for i in range(1, len(stock_list)):
        if stock_list[i] < buy:
            buy = stock_list[i]
            sell = 0
        elif stock_list[i] > sell:
            sell = stock_list[i]
            profit = max(profit, sell - buy)

    return profit

# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))