# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 320,
    "AMZN": 150,
    "GOOG": 140
}

portfolio = {}
total_value = 0

print("📊 Simple Stock Portfolio Tracker")
print("Enter 'done' when you finish.\n")

while True:
    stock = input("Enter stock ticker (e.g., AAPL): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not recognized! Available:", ", ".join(stock_prices.keys()))
        continue

    try:
        qty = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Please enter a valid number.\n")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + qty
    print(f"Added {qty} shares of {stock}.\n")

# Calculate total investment
print("\n----- Portfolio Summary -----")
for stock, qty in portfolio.items():
    value = qty * stock_prices[stock]
    total_value += value
    print(f"{stock}: {qty} shares → ${value}")

print("\n💰 Total Investment Value:", total_value)
