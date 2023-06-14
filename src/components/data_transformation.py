from sklearn.impute import SimpleImputer ## HAndling Missing Values
from sklearn.preprocessing import StandardScaler # HAndling Feature Scaling
from sklearn.preprocessing import OrdinalEncoder # Ordinal Encoding
## pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import sys,os
from dataclasses import dataclass
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object


## Data Transformation config

@dataclass
class DataTransformationconfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

## Data Ingestionconfig class
class DataTransformation:
    def __init__(self):
                self.data_transformation_config=DataTransformationconfig()
    
    def get_data_transformation_object(self):
            try:
                    logging.info('get data transformation')
            except Exception as e:
                    logging.info("Error in Data Trnasformation")
                    raise CustomException(e,sys)

    def initiate_data_trans(self):
            try:
                      logging.info('Data transformation initate started')
            except Exception as e:
                      raise CustomException(e,sys)


            




