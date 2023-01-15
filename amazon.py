import pandas as pd


df = pd.read_csv("amazon_orders.csv")
df = df.fillna(0)  # Replace all "NA" values with "0"

print(f'Total Spent: £{df["Order Net Total"].sum()}')
print(f'Mean Spent: £{round(df["Order Net Total"].mean(), 2)}')
print(f'Max Spent: £{df["Order Net Total"].max()}')
print(f'Min Spent: £{df["Order Net Total"].min()}')

print()

print(f'Total purchases: {len(df)}')

# print the csv
# print(df.head())


