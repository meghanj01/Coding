def get_profit(stocks):
    max_profit = 0
    min_stock = 99999
    for i in stocks:
        min_stock = min(min_stock, i)
        max_profit = max(max_profit, i - min_stock)
    return max_profit


stocks = [7, 6, 4, 3, 1]
print(get_profit(stocks))
