import os
import sys
import pandas as pd

from src.logger import logging
from src.exception import CustomException

def load_raw_data(path: str) -> pd.DataFrame:
    try:
        logging.info("Starting Credit Card Fraud dataset ingestion")
        df = pd.read_csv(path)
        logging.info(
            f"Dataset loaded successfully with "
            f"{df.shape[0]} rows and {df.shape[1]} columns"
        )
        logging.info(
            f"Fraud class distribution: {df['Class'].value_counts().to_dict()}"
        )
        return df
    except Exception as e:
        logging.error(f"Error occurred during data ingestion: {e}")
        raise CustomException(e, sys)

if __name__ == "__main__":
    dataset_path = os.path.join("data", "raw", "creditcard.csv")
    df = load_raw_data(dataset_path)
    print("Dataset loaded successfully")
    print("Dataset shape:", df.shape)
    print("\nClass Distribution:")
    print(df["Class"].value_counts())
