import pandas as pd
import numpy as np
import sys
import os

from pathlib import Path

from src.DaimondPricePrediction.logger import logging
from src.DaimondPricePrediction.exceptions import CustomException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass


class DataIngestionConfig:
    raw_data_path = Path("artifacts/raw_data.csv")
    train_data_path = Path("artifacts/train_data.csv") 
    test_data_path = Path("artifacts/test_data.csv")



class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started..")
        try:
            data = pd.read_csv(Path("notebooks/data/gemstone.csv"))
            logging.info("dataset readed as dataframe")

            folder,file = os.path.split(self.ingestion_config.raw_data_path)
            Path(folder).mkdir(exist_ok=True,parents=True)

            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("raw data saved to artifacts")

            train_data,test_data = train_test_split(data,test_size=0.2)
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            logging.info("train data csv stored to artifact")

            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("test data csv stores to artifacts")

            logging.info("Data ingestion completed")

            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path)


        except Exception as e:
            logging.info("An Exception occured during data ingestion")
            raise CustomException(e,sys)
    
if __name__ == '__main__':
    data_ingestion_obj = DataIngestion()
    data_ingestion_obj.initiate_data_ingestion()
