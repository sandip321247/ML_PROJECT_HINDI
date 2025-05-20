from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig 
import sys


if __name__=="__main__":
    logging.info("The execution has started")    

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        #data_ingestion_config = DataIngestionConfig()
    except Exception as e:
        logging.error("Error occurred")
        raise CustomException(e,sys) 