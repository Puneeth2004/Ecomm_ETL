import pandas as pd


def convert_dates(dataframe):
    """
    Convert all date columns to datetime.
    """

    date_columns = [

        "signup_date",
        "order_date",
        "payment_date",
        "shipping_date",
        "delivery_date",
        "review_date",
        "return_date",
        "last_restock_date"

    ]

    for column in date_columns:

        if column in dataframe.columns:

            original = dataframe[column].copy()

            pd.to_datetime(
                dataframe[column],
                errors="coerce"
            )

            invalid_rows = dataframe[
                dataframe[column].isna() &
                original.notna()
            ]

            if not invalid_rows.empty:

                print(f"\n[WARNING] Invalid values found in '{column}'")
                print(invalid_rows[[column]].head())
                print(f"Total Invalid {column}: {len(invalid_rows)}")

    return dataframe


def remove_invalid_mandatory_dates(dataframe):
    """
    Remove rows having invalid mandatory dates.
    """

    mandatory_dates = [

        "signup_date",
        "order_date",
        "payment_date",
        "shipping_date"

    ]

    for column in mandatory_dates:

        if column in dataframe.columns:

            before = len(dataframe)

            dataframe = dataframe.dropna(
                subset=[column]
            )

            removed = before - len(dataframe)

            if removed > 0:

                print(
                    f"[INFO] Removed {removed} rows due to invalid '{column}'"
                )

    return dataframe


def clean_text(dataframe):
    """
    Remove leading/trailing spaces.
    """

    text_columns = dataframe.select_dtypes(
        include="object"
    ).columns

    for column in text_columns:

        dataframe[column] = (

            dataframe[column]

            .astype(str)

            .str.strip()

        )

    return dataframe


def clean_emails(dataframe):
    """
    Convert email addresses to lowercase.
    """

    if "email" in dataframe.columns:

        dataframe["email"] = (

            dataframe["email"]

            .str.lower()

            .str.strip()

        )

    return dataframe


def fill_missing_values(dataframe):
    """
    Fill selected missing values.
    """

    fill_values = {

        "city": "Unknown",

        "carrier": "Unknown",

        "payment_method": "Unknown",

        "return_reason": "Not Provided"

    }

    for column, value in fill_values.items():

        if column in dataframe.columns:

            dataframe[column] = dataframe[column].fillna(value)

    return dataframe


def remove_duplicate_rows(dataframe):
    """
    Remove duplicate rows.
    """

    return dataframe.drop_duplicates()


def remove_duplicate_emails(dataframe):
    """
    Remove duplicate email addresses.
    """

    if "email" in dataframe.columns:

        before = len(dataframe)

        dataframe = dataframe.drop_duplicates(
            subset=["email"],
            keep="first"
        )

        removed = before - len(dataframe)

        if removed > 0:

            print(
                f"[INFO] Removed {removed} duplicate email records."
            )

    return dataframe

 
def transform_data(datasets):
    """
    Apply all transformations.
    """

    transformed_datasets = {}

    for dataset_name, dataframe in datasets.items():

        print(f"\nTransforming '{dataset_name}'...")

        dataframe = dataframe.copy()

        dataframe = convert_dates(dataframe)

        dataframe = remove_invalid_mandatory_dates(dataframe)

        dataframe = clean_text(dataframe)

        dataframe = clean_emails(dataframe)

        dataframe = fill_missing_values(dataframe)

        dataframe = remove_duplicate_rows(dataframe)

        dataframe = remove_duplicate_emails(dataframe)


        transformed_datasets[dataset_name] = dataframe

    return transformed_datasets