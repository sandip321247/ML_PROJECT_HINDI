from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys


if __name__=="__main__":
    logging.info("Starting the ML project")    

    try:
        a=1/0
    except Exception as e:
        logging.error("Error occurred")
        raise CustomException(e,sys) 