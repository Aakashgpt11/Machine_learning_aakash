# all the code related to reading the data
import os
import sys
import pandas as pd 

from dataclasses import dataclass
from sklearn.model_selection import train_test_split

print('aakash')
from src.exception import CustomException
import logging


# here we are configurating the raw data as input 
# it tell where to save the train test data as output 
# making a decorator for the data
@dataclass
class DataIngestionConfig:
#     """Data Ingestion Configuration class"""
    train_data_path: str = os.path.join('artifacts','train.csv')
    test_data_path: str = os.path.join('artifacts','test.csv')
    raw_data_path: str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    
    # for initiating and creating subobjects on calling of DataIngestion
    def __init__(self):
      self.ingestion_config = DataIngestionConfig()
    
    # for reading the data from the databases
    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method or component')
        try:
            # jahan se bhi data read krna hai uska path
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            # for the training data if exists then doesnot replace just modify it otherwise make new directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            # sending the file to csv
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info('Train test split initiated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header = True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header = True)

            logging.info('Imgestion of the data is completed')
            
            # we are returning this for the next step 
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            print('in the exception block')
            raise CustomException(e,sys)
        
        
if __name__ == "__main__":
       print(sys)
       obj = DataIngestion()
       obj.initiate_data_ingestion()

