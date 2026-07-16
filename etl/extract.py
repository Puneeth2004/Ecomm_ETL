import os
import pandas as pd


def extract_data(data_path):
    """
    Read all CSV files from the raw data folder.

    Parameters
    ----------
    data_path : str
        Path to the raw data folder.

    Returns
    -------
    dict
        Dictionary of DataFrames.
    """

    datasets = {}

    csv_files = [
        file
        for file in os.listdir(data_path)
        if file.endswith(".csv")
    ]

    for file in csv_files:

        file_path = os.path.join(data_path, file)

        dataframe = pd.read_csv(file_path)

        dataset_name = os.path.splitext(file)[0]

        datasets[dataset_name] = dataframe

    return datasets