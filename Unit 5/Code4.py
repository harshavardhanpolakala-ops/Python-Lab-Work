
import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
data = pd.read_csv("sales.csv")

# Calculate total sales
data["Total"] = data["Quantity"] * data["Price"]

print("\n--- RETAIL SALES DASHBOARD ---")
print(data)

print("\nTotal Sales:", data["Total"].sum())
print("Total Quantity Sold:", data["Quantity"].sum())

# Sales by product
product_sales = data.groupby("Product")["Total"].sum()

# Bar chart
plt.figure(figsize=(8, 5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Pie chart
plt.figure(figsize=(6, 6))
product_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Product Sales Percentage")
plt.ylabel("")
plt.show()
