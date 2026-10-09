import pandas as pd


# Read data
df = pd.read_csv("financial_data.csv")

# Calculate ratios
df["ROA"] = (df["ni"] / df["at"]) * 100
df["ROE"] = (df["ni"] / df["seq"]) * 100∏

# Show results
print(df[["tic", "fyear", "ROA", "ROE"]])