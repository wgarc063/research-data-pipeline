import pandas as pd

# Load raw data
df = pd.read_csv("input_data.csv")

print("Raw Data:")
print(df)

# Clean data
df["Name"] = df["Name"].str.title()  # Standardize names
df = df.drop_duplicates()  # Remove duplicates
df = df.fillna("N/A")  # Handle missing values

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned Data saved to cleaned_data.csv")
