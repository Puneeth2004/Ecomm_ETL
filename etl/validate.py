import re
import pandas as pd


def check_missing_values(dataframe):
    """
    Returns total missing values.
    """
    return dataframe.isnull().sum().sum()


def check_duplicate_rows(dataframe):
    """
    Returns duplicate row count.
    """
    return dataframe.duplicated().sum()


def check_duplicate_emails(dataframe):
    """
    Returns duplicate email count.
    """

    if "email" not in dataframe.columns:
        return 0

    return dataframe["email"].duplicated().sum()


def check_invalid_emails(dataframe):
    """
    Returns invalid email count.
    """

    if "email" not in dataframe.columns:
        return 0

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    invalid = 0

    for email in dataframe["email"].dropna():

        if not re.match(pattern, str(email)):
            invalid += 1

    return invalid


def check_negative_prices(dataframe):

    if "cost_price" not in dataframe.columns:
        return 0

    return (
        (dataframe["cost_price"] < 0).sum()
        +
        (dataframe["selling_price"] < 0).sum()
    )


def check_loss_products(dataframe):

    if "cost_price" not in dataframe.columns:
        return 0

    return (
        dataframe["selling_price"]
        <
        dataframe["cost_price"]
    ).sum()


def check_negative_quantity(dataframe):

    if "quantity" not in dataframe.columns:
        return 0

    return (dataframe["quantity"] < 0).sum()


def check_invalid_rating(dataframe):

    if "rating" not in dataframe.columns:
        return 0

    return (
        (dataframe["rating"] < 1)
        |
        (dataframe["rating"] > 5)
    ).sum()


def validate_data(datasets):
    """
    Validate all datasets.
    """

    report = []

    for dataset_name, dataframe in datasets.items():

        report.append({

            "Dataset": dataset_name,

            "Rows": len(dataframe),

            "Columns": len(dataframe.columns),

            "Missing Values":
                check_missing_values(dataframe),

            "Duplicate Rows":
                check_duplicate_rows(dataframe),

            "Duplicate Emails":
                check_duplicate_emails(dataframe),

            "Invalid Emails":
                check_invalid_emails(dataframe),

            "Negative Prices":
                check_negative_prices(dataframe),

            "Loss Products":
                check_loss_products(dataframe),

            "Negative Quantity":
                check_negative_quantity(dataframe),

            "Invalid Ratings":
                check_invalid_rating(dataframe)

        })

    return pd.DataFrame(report)