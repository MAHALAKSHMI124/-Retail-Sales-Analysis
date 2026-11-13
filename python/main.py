
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/retail_sales_raw.csv")


# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Convert Order Date into datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Check updated data types
print("\nUpdated Data Types:")
print(df.dtypes)



# BUSINESS KPI ANALYSIS

total_revenue = df["Sales"].sum()

total_profit = df["Profit"].sum()

total_orders = df["Order ID"].nunique()

total_quantity = df["Quantity"].sum()

average_order_value = total_revenue / total_orders

# Display results

print("\n========== BUSINESS KPI REPORT ==========")

print("Total Revenue:", round(total_revenue, 2))

print("Total Profit:", round(total_profit, 2))

print("Total Orders:", total_orders)

print("Total Quantity Sold:", total_quantity)

print("Average Order Value:", round(average_order_value, 2))



# CATEGORY-WISE SALES ANALYSIS

category_sales = df.groupby("Category")["Sales"].sum()

print("\nCATEGORY-WISE REVENUE")
print(category_sales.sort_values(ascending=False))

# Category-wise profit
category_profit = df.groupby("Category")["Profit"].sum()

print("\nCATEGORY-WISE PROFIT")
print(category_profit.sort_values(ascending=False))

# Category-wise quantity
category_quantity = df.groupby("Category")["Quantity"].sum()

print("\nCATEGORY-WISE QUANTITY")
print(category_quantity.sort_values(ascending=False))




# CATEGORY-WISE REVENUE CHART

plt.figure(figsize=(10, 5))

category_sales.sort_values(ascending=False).plot(
    kind="bar",
    title="Revenue by Product Category"
)

plt.xlabel("Product Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))

category_profit.sort_values(ascending=False).plot(
    kind="bar",
    title="Profit by Product Category"
)

plt.xlabel("Product Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()



# REGION-WISE REVENUE ANALYSIS

region_sales = df.groupby("Region")["Sales"].sum()

print("\nREGION-WISE REVENUE")
print(region_sales.sort_values(ascending=False))



# HIGHEST REVENUE REGION
highest_region = region_sales.idxmax()

# LOWEST REVENUE REGION
lowest_region = region_sales.idxmin()

print("\nHighest Revenue Region:", highest_region)
print("Lowest Revenue Region:", lowest_region)



import matplotlib.pyplot as plt

plt.figure(figsize=(9, 5))

region_sales.sort_values().plot(
    kind="bar",
    title="Region-wise Revenue Analysis"
)

plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Convert Series into DataFrame
region_df = region_sales.reset_index(name="Total Sales")

# Create Seaborn bar chart
plt.figure(figsize=(9, 5))

sns.barplot(
    data=region_df,
    x="Region",
    y="Total Sales"
)

plt.title("Region-wise Revenue Comparison")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()



print("\nAVAILABLE COLUMNS:")
print(df.columns.tolist())



# CUSTOMER SEGMENT ANALYSIS

segment_sales = df.groupby("Customer Segment")["Sales"].sum()

print("\nSEGMENT-WISE REVENUE")
print(segment_sales.sort_values(ascending=False))

# Highest revenue segment
highest_segment = segment_sales.idxmax()

print("\nHighest Revenue Segment:", highest_segment)

# Visualization
segment_df = segment_sales.reset_index(name="Total Sales")

plt.figure(figsize=(8, 5))

sns.barplot(
    data=segment_df,
    x="Customer Segment",
    y="Total Sales"
)

plt.title("Customer Segment-wise Revenue")
plt.xlabel("Customer Segment")
plt.ylabel("Total Revenue")

plt.tight_layout()
plt.show()



# SEGMENT-WISE REVENUE CONTRIBUTION

total_revenue = df["Sales"].sum()

segment_percentage = (segment_sales / total_revenue) * 100

print("\nSEGMENT REVENUE CONTRIBUTION (%)")
print(segment_percentage.round(2))



# SUB-CATEGORY REVENUE ANALYSIS

subcategory_sales = df.groupby("Sub-Category")["Sales"].sum()

print("\nSUB-CATEGORY-WISE REVENUE")

print(subcategory_sales.sort_values(ascending=False))




# FIND HIGHEST AND LOWEST REVENUE SUB-CATEGORY

highest_product = subcategory_sales.idxmax()
lowest_product = subcategory_sales.idxmin()

print("\nHighest Revenue Sub-Category:", highest_product)
print("Highest Revenue:", subcategory_sales.max())

print("\nLowest Revenue Sub-Category:", lowest_product)
print("Lowest Revenue:", subcategory_sales.min())



# SUB-CATEGORY PROFIT ANALYSIS

subcategory_profit = df.groupby("Sub-Category")["Profit"].sum()

print("\nSUB-CATEGORY-WISE PROFIT")

print(subcategory_profit.sort_values(ascending=False))

print("\nHighest Profit Sub-Category:", subcategory_profit.idxmax())
print("Lowest Profit Sub-Category:", subcategory_profit.idxmin())




subcategory_df = subcategory_sales.reset_index(name="Total Sales")

plt.figure(figsize=(12, 6))

sns.barplot(
    data=subcategory_df.sort_values("Total Sales", ascending=False),
    x="Sub-Category",
    y="Total Sales"
)

plt.title("Sub-Category-wise Revenue Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# SUB-CATEGORY PROFIT ANALYSIS

subcategory_profit = df.groupby("Sub-Category")["Profit"].sum()

print("\nSUB-CATEGORY-WISE PROFIT")
print(subcategory_profit.sort_values(ascending=False))

# Highest profit sub-category
highest_profit_product = subcategory_profit.idxmax()

# Lowest profit sub-category
lowest_profit_product = subcategory_profit.idxmin()

print("\nHighest Profit Sub-Category:", highest_profit_product)
print("Highest Profit:", subcategory_profit.max())

print("\nLowest Profit Sub-Category:", lowest_profit_product)
print("Lowest Profit:", subcategory_profit.min())




# SUB-CATEGORY PROFIT VISUALIZATION

profit_df = subcategory_profit.reset_index(name="Total Profit")

plt.figure(figsize=(12, 6))

sns.barplot(
    data=profit_df.sort_values("Total Profit", ascending=False),
    x="Sub-Category",
    y="Total Profit"
)

plt.title("Sub-Category-wise Profit Analysis")
plt.xlabel("Sub-Category")
plt.ylabel("Total Profit")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# DISCOUNT ANALYSIS

print("\nUNIQUE DISCOUNT VALUES")

print(sorted(df["Discount"].dropna().unique()))



# DISCOUNT-WISE REVENUE AND PROFIT

discount_analysis = df.groupby("Discount").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
)

print("\nDISCOUNT-WISE ANALYSIS")

print(discount_analysis.round(2))



# DISCOUNT VS PROFIT VISUALIZATION

plt.figure(figsize=(9, 5))

sns.barplot(
    data=discount_analysis.reset_index(),
    x="Discount",
    y="Total_Profit"
)

plt.title("Impact of Discount on Profit")
plt.xlabel("Discount")
plt.ylabel("Total Profit")

plt.tight_layout()
plt.show()


# SHIPPING MODE ANALYSIS

shipping_analysis = df.groupby("Ship Mode").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum"),
    Total_Quantity=("Quantity", "sum"),
    Total_Orders=("Order ID", "nunique")
)

print("\nSHIPPING MODE ANALYSIS")
print(shipping_analysis.round(2))



# HIGHEST AND LOWEST REVENUE SHIPPING MODE

highest_shipping = shipping_analysis["Total_Sales"].idxmax()
lowest_shipping = shipping_analysis["Total_Sales"].idxmin()

print("\nHighest Revenue Shipping Mode:", highest_shipping)
print("Lowest Revenue Shipping Mode:", lowest_shipping)

# HIGHEST PROFIT SHIPPING MODE

highest_profit_shipping = shipping_analysis["Total_Profit"].idxmax()

print("\nHighest Profit Shipping Mode:", highest_profit_shipping)



# SHIPPING MODE REVENUE VISUALIZATION

shipping_df = shipping_analysis.reset_index()

plt.figure(figsize=(9, 5))

sns.barplot(
    data=shipping_df,
    x="Ship Mode",
    y="Total_Sales"
)

plt.title("Shipping Mode-wise Revenue Analysis")
plt.xlabel("Shipping Mode")
plt.ylabel("Total Revenue")

plt.tight_layout()
plt.show()



# CORRELATION ANALYSIS

numeric_df = df.select_dtypes(include="number")

print("\nNUMERICAL COLUMNS")
print(numeric_df.columns.tolist())



correlation = numeric_df.corr()

print("\nCORRELATION MATRIX")
print(correlation.round(2))



plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()


# BUSINESS INSIGHTS REPORT

print("\n========== BUSINESS INSIGHTS ==========")

# 1. Highest revenue category
print(
    "Highest Revenue Category:",
    category_sales.idxmax()
)

# 2. Highest profit category
print(
    "Highest Profit Category:",
    category_profit.idxmax()
)

# 3. Highest revenue region
print(
    "Highest Revenue Region:",
    region_sales.idxmax()
)

# 4. Highest revenue customer segment
print(
    "Highest Revenue Customer Segment:",
    segment_sales.idxmax()
)

# 5. Highest revenue sub-category
print(
    "Highest Revenue Sub-Category:",
    subcategory_sales.idxmax()
)

# 6. Highest profit sub-category
print(
    "Highest Profit Sub-Category:",
    subcategory_profit.idxmax()
)

# 7. Highest revenue shipping mode
print(
    "Highest Revenue Shipping Mode:",
    shipping_analysis["Total_Sales"].idxmax()
)

print("=======================================")



# EXPORT CLEANED DATASET

df.to_csv("cleaned_retail_sales.csv", index=False)

print("\nCleaned dataset exported successfully!")
