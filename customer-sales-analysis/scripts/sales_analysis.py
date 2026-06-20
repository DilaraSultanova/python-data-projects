import pandas as pd

# Load sales data
df = pd.read_csv("sample_data/sales_data.csv")

# Calculate metrics
total_revenue = df["Revenue"].sum()

category_revenue = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_products = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Display results
print("=" * 40)
print("CUSTOMER SALES ANALYSIS")
print("=" * 40)

print(f"\nTotal Revenue: ${total_revenue}")

print("\nRevenue by Category")
print(category_revenue)

print("\nTop Products")
print(top_products)

print("\nAnalysis Complete")
