import pandas as pd

# Load raw data
df = pd.read_csv("data/raw/jobs_raw.csv")

# Drop columns with more than 50% missing values
df = df.dropna(axis=1, thresh=len(df) * 0.5)

# Drop duplicate rows
df = df.drop_duplicates()

# Clean text columns
if 'title' in df.columns:
    df['title'] = df['title'].str.strip().str.lower()

# Save cleaned data
df.to_csv("data/clean/jobs_clean.csv", index=False)

print("Data cleaning complete. Cleaned file saved to data/clean/jobs_clean.csv")

