from src.data_ingestion.loader import load_aws_cloudwatch_data

data = load_aws_cloudwatch_data("aws_cloudwatch_data")
print("Loaded files:", list(data.keys()))
for k, df in data.items():
    print(f"{k}: shape {df.shape}, columns: {list(df.columns)}")