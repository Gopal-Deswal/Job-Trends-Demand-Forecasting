import pandas as pd
import argparse

def load_raw(input_path):
    """Load raw job postings from JSON or CSV file."""
    if input_path.endswith(".json"):
        return pd.read_json(input_path, lines=True)
    elif input_path.endswith(".csv"):
        return pd.read_csv(input_path)
    else:
        raise ValueError("Unsupported file format. Use .json or .csv")

def save_raw(df, output_path):
    """Save DataFrame to CSV."""
    df.to_csv(output_path, index=False)

def main():
    parser = argparse.ArgumentParser(description="Ingest raw job postings data")
    parser.add_argument("--input_path", required=True, help="Path to raw data file (JSON or CSV)")
    parser.add_argument("--output_path", required=True, help="Path to save output CSV")
    args = parser.parse_args()

    df = load_raw(args.input_path)
    save_raw(df, args.output_path)
    print(f"Loaded {len(df)} rows and saved to {args.output_path}")

if __name__ == "__main__":
    main()

