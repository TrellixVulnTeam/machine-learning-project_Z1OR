
from re import X
from tkinter import E

from sklearn.model_selection import train_test_split
from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import sys,os



class DataValidation:
    

    def __init__(self,data_validation_config:DataValidationConfig,
        data_ingestion_artifact:DataIngestionArtifact):
        try:
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e

    def is_train_test_file_exists(self)-> bool:
        try:
            logging.info("Checking if training and test file are available")
            is_train_file_exist=False
            is_test_file_exist=False

            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            is_train_file_exist=os.path.exists(train_file_path)
            is_test_file_exist=os.path.exists(test_file_path)

            is_available=is_train_file_exist and is_test_file_exist
            logging.info(f"Is train and test file exist? -> {is_available}")

            is_available=self.is_train_test_file_exists()
            if not is_available:
                training_file=self.data_ingestion_artifact.train_file_path
                testing_file=self.data_ingestion_artifact.test_file_path
                
                message =f"Training file :{training_file} or test file: {testing_file} is not present"
                logging.info(message)
                raise Exception(message)
            return is_available
        except Exception as e:
            raise HousingException(e,sys) from e


    def validate_dataset_schema(self)-> bool:
        try:
            validation_status=False

            validation_status=True

            return validation_status
        except Exception as e:
            raise HousingException(e,sys) from e

    def initiate_data_validation(self):
        try:
            self.is_train_test_file_exists()
            self.validate_dataset_schema()
        except Exception as e:
            raise HousingException(e,sys) from e