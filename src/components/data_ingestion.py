import os
import sys
from src.exception import CustomException
from src.logger import logging
#python from logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Defining the input for data Ingestion componet first
@dataclass # it will help direct define class veriable with initializing (self)
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')


class DataIngestion:
    def __init__(self) -> None:
        self.initiate_config = DataIngestionConfig()
        
    
    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method or component')
        
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as DataFrame')

            os.makedirs(os.path.dirname(self.initiate_config.train_data_path),exist_ok=True)
            
            #saving raw data file
            df.to_csv(self.initiate_config.raw_data_path,index=False,header=True)
            
            logging.info('Train Test split initiated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            
            #savng train & test file
            train_set.to_csv(self.initiate_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.initiate_config.test_data_path,index=False,header=True)
            
            logging.info('Ingestion of data is Completed')
            
            return(
                self.initiate_config.train_data_path,
                self.initiate_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion() # test data_ingestion.py only        
            
            


     