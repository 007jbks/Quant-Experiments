import pandas as pd
import matplotlib.pyplot as plt

data['Date'] = pd.to_datetime(data['Date'])


filtered_data = data[data['Date'] >= pd.Timestamp('2004-08-10')]


dates = filtered_data['Date'].tolist()
adj_close_prices = filtered_data['Adj Close'].tolist()

initial_price = adj_close_prices[0]
base_price = initial_price
cash = 0
tax_rate = 0.2

prices = []
wealth = []


for current_price in adj_close_prices:
    if current_price >= 1.1 * base_price:
        profit = 0.1 * current_price * (1 - tax_rate)
        cash += profit
        current_price *= 0.9
        base_price = current_price

    prices.append(current_price)
    wealth.append(current_price + cash)


plt.figure(figsize=(12, 6))
plt.plot(dates, wealth, label="Wealth over time", color='blue')
plt.plot(dates, adj_close_prices, label="Original Adj Close Price", color='red')
plt.title("Profit Skimming Strategy with Tax (20%)")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("Final Wealth:", wealth[-1])
print(adj_close_prices[0])
