import kagglehub
from kagglehub import KaggleDatasetAdapter

def extract():
    print("Extracting data from Kaggle...")
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        "rohitgrewal/quick-commerce-dataset",
        "quick_commerce_data_modified_cleaned.csv",
    )
    print(f"Extracted {len(df):,} rows")
    return df

if __name__ == "__main__":
    df = extract()
    print(df.head())