import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv('/Users/nihalr/Downloads/Fruit-Prices-2022.csv')

# Question 1: Calculate the average price of each fruit
average_prices = data.groupby('Fruit')['RetailPrice'].mean()
print("Average Prices:\n", average_prices)

# Question 2: Filter fruits with prices above a threshold
threshold = 5.00
expensive_fruits = data[data['RetailPrice'] > threshold]
print("Expensive Fruits:\n", expensive_fruits)

# Question 4: Identify least expensive fruits
least_expensive = data.loc[data['RetailPrice'].idxmin()]
print("Least Expensive Fruit:\n", least_expensive)

# Question 5: most expensive fruit
most_expensive = data.loc[data['RetailPrice'].idxmax()]
print("Most Expensive Fruit:\n", most_expensive)

# Question 6: which form is the most expensive
average_price_by_form = data.groupby('Form')['RetailPrice'].mean()
most_expensive_form = average_price_by_form.idxmax()
highest_price = average_price_by_form.max()
print("Most Expensive Form:", most_expensive_form)
print("Average Price of Most Expensive Form:", highest_price)

# Plot the average price of fruits by form
avg_price_by_form = data.groupby('Form')['RetailPrice'].mean()
avg_price_by_form.plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Average Price of Fruits by Form', fontsize=16)
plt.xlabel('Fruit Form', fontsize=12)
plt.ylabel('Average Price (per unit)', fontsize=12)
plt.tight_layout()  # Makes lables fit within plot
plt.show()