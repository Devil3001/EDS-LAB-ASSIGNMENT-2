#Advanced Data Manipulation
#1. Combining Data (Merge & Concatenate)
df1 = pd.DataFrame({"ID": [1,2], "Name": ["A", "B"]})
df2 = pd.DataFrame({"ID": [1,2], "Salary": [30000, 40000]})

merged = pd.merge(df1, df2, on="ID")
print(merged)

combined = pd.concat([df1, df1])
print(combined)

#2. Time Series Data Handling
df.set_index("Order Date", inplace=True)

# Monthly sales trend
monthly_trend = df["Sales"].resample("M").sum()
print(monthly_trend)
