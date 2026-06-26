import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("supermarket_sales.csv")

# Display first rows
print(df.head())

# Total sales
print("Total Sales:", df["Total"].sum())

# Top Product Line
print(df["Product line"].value_counts())

# Sales by Product Line
df.groupby("Product line")["Total"].sum().plot(kind="bar")
plt.title("Sales by Product Line")
plt.show()