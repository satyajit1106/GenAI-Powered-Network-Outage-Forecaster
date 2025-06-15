import os
import pandas as pd
from typing import Dict

def load_aws_cloudwatch_data(
    directory: str = "aws_cloudwatch_data"
) -> Dict[str, pd.DataFrame]:
    
    """
    Loads all CSV files in the specified aws_cloudwatch_data directory into a dictionary of DataFrames.
    Each key is the file name (without extension), value is the corresponding DataFrame.
    Assumes each CSV contains at least a 'timestamp' column.
    
    Parameters:
    - directory (str): Path to the folder containing AWS CloudWatch CSV files.

    Returns:
    - Dict[str, pd.DataFrame]: Dictionary mapping file names to DataFrames.
    """
    
    data = {}
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")
    
    files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    if not files:
        raise FileNotFoundError(f"No CSV files found in directory '{directory}'.")

    for fname in files:
        path = os.path.join(directory, fname)
        try:
            df = pd.read_csv(path)
            # Try to parse timestamp if present
            if 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
            key = os.path.splitext(fname)[0]
            data[key] = df
        except Exception as e:
            print(f"Error loading {path}: {e}")
            continue

    return data

# Example usage:
if __name__ == "__main__":
    data = load_aws_cloudwatch_data("aws_cloudwatch_data")
    for name, df in data.items():
        print(f"{name}: {df.shape} rows")