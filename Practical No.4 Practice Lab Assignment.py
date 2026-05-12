
import pandas as pd

# Create DataFrame
data = {
    "Name": ["Amit", "Neha", "Ravi", "Priya"],
    "Age": [21, 22, 20, 23],
    "Marks": [78, 85, 69, 90]
}

df = pd.DataFrame(data)

# Display
print(df)

# Basic operations
print("Head:\n", df.head())
print("Tail:\n", df.tail())
print("Shape:", df.shape)
print("Columns:", df.columns)
print("Data Types:\n", df.dtypes)

# Selection
print(df["Marks"])
print(df.loc[1])
print(df.iloc[2])

# Sorting
print(df.sort_values("Marks"))

# Filtering
print(df[df["Marks"] > 80])

# Add column
df["Result"] = ["Pass", "Pass", "Pass", "Pass"]

# Drop column
df.drop("Age", axis=1, inplace=True)

print("Updated DataFrame:\n", df)
