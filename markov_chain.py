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
initial_price = 100
prices = []
for i in price:
    if i=='U':
        initial_price+=1
        prices.append(initial_price)
    else:
        initial_price-=1
        prices.append(initial_price)
# Now let's make the Markov Chain
num_from_U_to_D = 0
num_from_U_to_U = 0
num_from_D_to_D = 0
num_from_D_to_U = 0
def func():
    for i in range(len(price[:100])-1):
        if price[i]=='U' and price[i+1]=='D':
            global num_from_U_to_D
            num_from_U_to_D+=1
        elif price[i]=='U' and price[i+1]=='U':
            global num_from_U_to_U
            num_from_U_to_U+=1
        elif price[i]=='D' and price[i+1]=='U':
            global num_from_D_to_U
            num_from_D_to_U+=1
        elif price[i]=='D' and price[i+1]=='D':
            global num_from_D_to_D
            num_from_D_to_D+=1
num_U = price[:100].count('U')
num_D = price[:100].count('D')
func()
markov_chain = {
    'U':{
        'U':num_from_U_to_U/num_U,
        'D':num_from_D_to_U/num_D
    },
    'D':{
        'U':num_from_U_to_D/num_U,
        'D':num_from_D_to_D/num_D       
    }
}

markov_chain = pd.DataFrame(markov_chain)
print(markov_chain.round(2)) 

# Predict 1000 steps
predicted_prices = []
base = prices[99] 
initial_condition = price[99] 

for _ in range(1000):  
    probs = markov_chain[initial_condition]
    next_state = random.choices(
        population=['U', 'D'],
        weights=[probs['U'], probs['D']]
    )[0]
    base += 1 if next_state == 'U' else -1
    predicted_prices.append(base)
    initial_condition = next_state

I = list(range(100, 1100))          
actual_prices = prices[100:1100]    



import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(I, actual_prices, color='red', label='Actual Price')
plt.plot(I, predicted_prices, color='blue', label='Predicted Price')
plt.title("Markov Chain Prediction vs Actual Price (Steps 100–1099)")
plt.xlabel("Step")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()

