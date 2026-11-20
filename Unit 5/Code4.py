
import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the folder where this Python file is located
folder = os.path.dirname(os.path.abspath(__file__))

# Read sales data
data = pd.read_csv(os.path.join(folder, "sales.csv"))

# Calculate total sales
data["Total"] = data["Quantity"] * data["Price"]

# Display sales report
print("RETAIL SALES DASHBOARD")
print("----------------------")
print(data)

print("\nTotal Sales:", data["Total"].sum())
print("Highest Selling Product:",
      data.loc[data["Total"].idxmax(), "Product"])

# Bar chart
plt.figure(figsize=(8, 5))
plt.bar(data["Product"], data["Total"])
plt.title("Product-wise Sales")
plt.xlabel("Products")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Pie chart
plt.figure(figsize=(7, 7))
plt.pie(data["Total"], labels=data["Product"], autopct="%1.1f%%")
plt.title("Sales Distribution")
plt.show()
