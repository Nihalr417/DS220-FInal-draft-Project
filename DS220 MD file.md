# Fruit Price Analysis: 2022 Dataset

## Introduction

In this project, we analyze a dataset containing the prices of different fruits sold in various forms, such as fresh, sliced, or dried. The main goal of this analysis is to explore the prices of fruits in 2022 using Python, particularly the Pandas and Matplotlib libraries. By working with this dataset, we aim to discover important insights about fruit pricing, such as which fruits are more expensive, which are cheaper, and which forms of fruits are priced higher. Fruits are really important and an healthy alternative to junkfood, so learning about it is really important.

Pandas helps us organize and manipulate the data, while Matplotlib allows us to create visualizations that make it easier to understand the results.

## Data Preprocessing

Before starting the analysis, We need to load the dataset.

```python
import pandas as pd

# Load the dataset
data = pd.read_csv('/path/to/Fruit-Prices-2022.csv')

# Display the first few rows to see the structure of the dataset
data.head()
The dataset has several columns, but the main ones we focus on for this analysis are:

Fruit: The type of fruit.
RetailPrice: The price of the fruit.
Form: The form in which the fruit is sold (e.g., fresh, sliced, dried).
We also check for any missing values to make sure the data is clean:

data.isnull().sum()
In this case, we found no missing values, so we can move ahead with the analysis without cleaning the data.

Next, we take a quick look at the price range by checking some basic statistics:

data['RetailPrice'].describe()
The summary statistics show us the minimum, maximum, mean, and standard deviation of fruit prices. This helps us understand how much the prices vary across different fruits.

Questions

1. Average Price of Each Fruit
Our first step is to calculate the average price of each fruit. This will tell us how much each fruit costs on average in 2022.

average_prices = data.groupby('Fruit')['RetailPrice'].mean()
print("Average Prices:\n", average_prices)
From this, we can see which fruits are generally more expensive and which are more affordable.

2. Expensive Fruits
Next, we want to find the fruits that are considered "expensive." We define "expensive" as any fruit with a price higher than $5.00.
threshold = 5.00
expensive_fruits = data[data['RetailPrice'] > threshold]
print("Expensive Fruits:\n", expensive_fruits)
This helps retailers and consumers identify fruits that may be more costly due to factors like seasonal availability, production costs, or rarity.

3. Least Expensive Fruit
We also want to know which fruit is the least expensive. This can be useful for shoppers who want to stick to a budget or businesses looking for affordable options.
least_expensive = data.loc[data['RetailPrice'].idxmin()]
print("Least Expensive Fruit:\n", least_expensive)
4. Most Expensive Fruit
On the flip side, we want to find out which fruit is the most expensive. This will show us which fruits are at the premium end of the market.

most_expensive = data.loc[data['RetailPrice'].idxmax()]
print("Most Expensive Fruit:\n", most_expensive)
5. Most Expensive Form
We also want to analyze the price difference between various forms of fruit. For example, is fresh fruit cheaper than sliced fruit? To answer this, we calculate the average price for each fruit form.
average_price_by_form = data.groupby('Form')['RetailPrice'].mean()
most_expensive_form = average_price_by_form.idxmax()
highest_price = average_price_by_form.max()
print("Most Expensive Form:", most_expensive_form)
print("Average Price of Most Expensive Form:", highest_price)

Visualization
To make our analysis easier to understand, we create a bar chart showing the average prices for each fruit form. This helps us visually compare the price differences between fresh, sliced, and dried fruits.

import matplotlib.pyplot as plt
avg_price_by_form = data.groupby('Form')['RetailPrice'].mean()
avg_price_by_form.plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Average Price of Fruits by Form', fontsize=16)
plt.xlabel('Fruit Form', fontsize=12)
plt.ylabel('Average Price (per unit)', fontsize=12)
plt.tight_layout()
plt.show()
This bar chart clearly shows us which fruit forms are more expensive on average, helping businesses and consumers make informed decisions.

Conclusion

From this analysis, we were able to uncover several key insights about fruit pricing in 2022:

Average Prices: Fruit prices vary widely. Some fruits, like exotic varieties, are much more expensive than others.
Expensive Fruits: We identified several fruits that cost more than $5, which are usually considered premium fruits.
Least and Most Expensive Fruits: The analysis revealed both the least and most expensive fruits, which can guide shoppers looking for either budget-friendly or high-end options.
Form Analysis: The form in which fruits are sold (e.g., fresh vs. sliced) plays a big role in their price, with some processed forms being more expensive on average.
These insights can help retailers, marketers, and consumers understand fruit pricing trends, make better decisions about which fruits to buy, and even influence pricing strategies in the supply chain.