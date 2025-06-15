import pandas as pd
import os

def load_aws_cloudwatch_data(directory: str):
    """
    Loads all CSV files in the given AWS Cloudwatch NAB directory into a dict of DataFrames.
    Each key is the file name (without extension), value is the DataFrame.
    """
    data = {}
    for fname in os.listdir(directory):
        if fname.endswith('.csv'):
            key = fname.replace('.csv', '')
            data[key] = pd.read_csv(os.path.join(directory, fname), parse_dates=['timestamp'])
    return data