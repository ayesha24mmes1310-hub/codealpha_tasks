# CodeAlpha Python Internship
# Task 2: Stock Portfolio Tracker
# Developed by: Ayesha Iqbal
# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320
}
# Variable to store total investment
total = 0
print("Available Stocks:")
for stock in stock_prices:
    print(stock)

# Taking input from user
while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        total = total + (stock_prices[stock_name] * quantity)
    else:
        print("Stock not found!")

# Displaying result
print("\nTotal Investment Value = $", total)

# Saving result in a text file
file = open("portfolio_result.txt", "w")
file.write("Total Investment Value = $" + str(total))
file.close()
print("Result saved in portfolio_result.txt")