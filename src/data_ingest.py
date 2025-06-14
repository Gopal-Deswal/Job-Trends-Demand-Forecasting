import pandas as pd
import os

source_file = "data/source/postings.csv"
output_file = "data/raw/jobs_raw.csv"

df = pd.read_csv(source_file)
os.makedirs(os.path.dirname(output_file), exist_ok=True)
df.to_csv(output_file, index=False)

print(f"✅ Ingested: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"✅ Saved to: {output_file}")
# Placeholder for data ingestion logic
