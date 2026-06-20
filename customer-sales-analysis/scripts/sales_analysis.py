import pandas as pd

# Load data
df = pd.read_csv("sample_data/sales_data.csv")

# Total revenue
total_revenue = df["Revenue"].sum()

# Revenue by category
category_revenue = df.groupby("Category")["Revenue"].sum()

# Top product
top_product = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("Total Revenue:")
print(total_revenue)

print("\nRevenue by Category:")
print(category_revenue)

print("\nTop Products:")
print(top_product)
