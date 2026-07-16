import os
import pandas as pd

DATA_PATH = "data/raw"

csv_files = [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]

print(csv_files)

datasets = {}
for file in csv_files:
    file_path = os.path.join(DATA_PATH, file)
    datasets[file] = pd.read_csv(file_path)

print(f"Loaded {len(datasets)} datasets successfully.")

print("\n" + "=" * 80)
print("DATASET PROFILING")
print("=" * 80)

for file_name, df in datasets.items():

    print("\n" + "-" * 60)
    print(f"Dataset: {file_name}")
    print("-" * 60)

    print(f"Shape: {df.shape}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print(f"\nDuplicate Rows: {df.duplicated().sum()}")

    for file_name, df in datasets.items():

        print("\n" + "=" * 80)
        print(f"DATASET : {file_name}")
        print("=" * 80)

        print(f"Shape : {df.shape}")

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print(f"\nDuplicate Rows : {df.duplicated().sum()}")

        print("\nFirst 5 Rows:")
        print(df.head())


        print(f"\nDuplicate Customer IDs : {df['customer_id'].duplicated().sum()}")