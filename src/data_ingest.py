import pandas as pd
import argparse
import os

def load_raw(input_path):
    """Load raw job data from CSV or JSON file."""
    ext = os.path.splitext(input_path)[1].lower()
    if ext == '.csv':
        return pd.read_csv(input_path)
    elif ext == '.json':
        return pd.read_json(input_path, lines=True)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def save_raw(df, output_path):
    """Save the DataFrame to output CSV file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest raw job data")
    parser.add_argument('--input_path', type=str, required=True, help='Path to raw input file (.csv or .json)')
    parser.add_argument('--output_path', type=str, required=True, help='Path to save processed output CSV')
    args = parser.parse_args()

    df = load_raw(args.input_path)
    save_raw(df, args.output_path)
    print(f"Raw data saved to {args.output_path}")

