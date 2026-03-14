stocks = {
    "AAPL":  180,
    "TSLA" : 250,
    "META" : 500,
    "NFLX" : 600,
    "NVDA" : 600,
}
portfolio = {}
investment = 0
user_input = int(input("Enter the number of stocks you want to buy:"))
while user_input != 0:
    stock_name = input("Enter the stock name you want to buy: ").upper()
    if stock_name in stocks:
        stock_quantity = int(input("Enter the quantity of stock you want to buy: "))
        if stock_name in portfolio:
            portfolio[stock_name] += stock_quantity
        else:
           portfolio[stock_name] = stock_quantity


        stock_value = stocks[stock_name] * stock_quantity
        investment = investment + stock_value
        user_input -= 1
    else:
        print("Stock does not exist")

print("Your stock portfolio is:",portfolio)
print("Your total investment in stocks is ",investment)