from etl.extract import extract_data
from etl.validate import validate_data
from etl.transform import transform_data
from etl.load import load_data

DATA_PATH = "data/raw"
REPORT_PATH = "reports/data_quality_report.csv"


def main():

    datasets = extract_data(DATA_PATH)
    report = validate_data(datasets)
    transformed_data = transform_data(datasets)
    report.to_csv(REPORT_PATH, index=False)
    load_data(transformed_data)
    print("ETL Pipeline Completed Successfully")

if __name__ == "__main__":
    main()