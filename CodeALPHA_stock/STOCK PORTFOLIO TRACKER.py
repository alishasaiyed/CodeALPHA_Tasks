# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130
}

total_investment = 0

print("📈 Stock Portfolio Tracker")

while True:

    # User input for stock name
    stock = input("Enter stock name (or type 'done' to finish): ").upper()

    # Stop loop
    if stock == "DONE":
        break

    # Check stock exists
    if stock not in stock_prices:
        print("❌ Stock not available!")
        continue

    # User input for quantity
    quantity = int(input("Enter quantity: "))

    # Calculate investment
    investment = stock_prices[stock] * quantity

    # Add to total
    total_investment += investment

    print(f"✅ {stock} added worth ${investment}")

# Display total investment
print("\n💰 Total Investment Value =", total_investment)

# Save result in text file
with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value = {total_investment}")

print("📁 Result saved in portfolio.txt")