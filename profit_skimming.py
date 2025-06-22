import numpy as np
import pandas as pd
import random
price = []
I = []
for i in range(2000):
    # stock = random.choice(['U','D'])
    stock = random.choices(['U', 'D'], weights=[0.55, 0.45])[0]

    price.append(stock)
    I.append(i)
initial_price = 1000
cash = 0
base_price = initial_price
prices = []
wealth = []

for move in price:
    if move == 'U':
        initial_price += 1
    else:
        initial_price -= 1

    # Check for 10% profit
    if initial_price >= 1.1 * base_price:
        profit = 0.1 * initial_price
        cash += profit
        initial_price *= 0.9
        base_price = initial_price

    prices.append(initial_price)
    wealth.append(initial_price + cash)
I = range(1,len(wealth)+1)
plt.plot(I,wealth,label="Wealth over time",color='blue')
plt.plot(I,prices,label="Stock price",color='red')
plt.show()
print(wealth[-1])
wealth_for_diff_Stat.append(wealth[-1])
