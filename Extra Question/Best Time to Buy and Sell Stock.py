def stock(prices):
    profit = 0
    buy = prices[0]
    for sell in prices:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell

    return profit

price = [7,1,5,3,6,4]

print(stock(price))