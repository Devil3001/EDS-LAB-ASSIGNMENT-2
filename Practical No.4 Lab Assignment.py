#Practical No.4 Lab Assignment
#Dataset: Sales Dataset (Real-Life Example)
from multiprocessing.sharedctypes import Value

import pandas as pd

df = pd.read_csv("sales_data.csv")
print(df.head())
#Assumed columns:
#Order ID, Product, Quantity Ordered, Price Each, Order Date, Purchase Address

#Data Cleaning
df.dropna(inplace=True)
df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"])
df["Price Each"] = pd.to_numeric(df["Price Each"])
df["Sales"] = df["Quantity Ordered"] * df["Price Each"]

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.month
df["City"] = df["Purchase Address"].apply(lambda x: x.split(",")[1])

#10 Sample Grains (Insights)
#Grain 1: Best Month for Sales
monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)

print("Best Month:", monthly_sales.idxmax())
print("Highest Sales:", monthly_sales.max())

#Grain 2: Product Sold the Most
product_qty = df.groupby("Product")["Quantity Ordered"].sum()
print(product_qty.sort_values(ascending=False).head(1))
#Reason: Low price and high daily demand.

#Grain 3: City with Highest Sales
city_sales = df.groupby("City")["Sales"].sum()
print(city_sales.sort_values(ascending=False))

#Grain 4: Products Sold Together
df_dup = df[df["Order ID"].duplicated(keep=False)]
df_dup["Grouped"] = df_dup.groupby("Order ID")["Product"].transform(lambda x: ",".join(x))
print(df_dup["Grouped"].value_counts().head())

#Grain 5: Average Sales per Order
print("Average Sales:", df["Sales"].mean())

#Grain 6: Maximum Single Order Value
print("Max Sale:", df["Sales"].max())
#Grain 7: Minimum Single Order Value
print("Min Sale:", df["Sales"].min())

#Grain 8: Total Revenue
print("Total Revenue:", df["Sales"].sum())

#Grain 9: Most Expensive Product
print(df.groupby("Product")["Price Each"].max().sort_values(ascending=False).head(1))

#Grain 10: Orders per City
print(df["City"].value_counts())

#Additional Grains (11–20) Using Pandas Methods
#11.	Median Sales
#12.	Standard Deviation of Sales
#13.	Month-wise Order Count
#14.	Product Count
#15.	City-wise Average Sales
#16.	Top 5 Products by Revenue
#17.	Bottom 5 Products by Revenue
#18.	Cumulative Sales
#19.	Sales Distribution using describe()
#20.	Data Correlation
print(df["Sales"].median())
print(df["Sales"].std())
print(df.groupby("Month").size())
print(df["Product"].nunique())
print(df.groupby("City")["Sales"].mean())
print(df.groupby("Product")["Sales"].sum().nlargest(5))
print(df.groupby("Product")["Sales"].sum().nsmallest(5))
print(df["Sales"].cumsum())
print(df.describe())
print(df.corr(numeric_only=True))
