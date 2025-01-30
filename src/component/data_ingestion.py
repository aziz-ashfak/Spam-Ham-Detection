import sys 
import pandas as pd
import numpy as np
import os
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
from sklearn.model_selection import train_test_split
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.exception import CustomException
from src.logger import logging
from src.utilts import save_data,load_data,text_preprocessing
from src.component.data_transformation import DataTransformationConfig
from src.component.data_transformation import DataTransfromation
from src.component.model_trainner import ModelTrainnerConfig
from src.component.model_trainner import ModelTrainner
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

class DataIngestionConfig:
    
    processing_df = os.path.join('artifacts','processing_data.csv')
    train_df = os.path.join('artifacts','train_data.csv')
    test_df = os.path.join('artifacts','test_data.csv')
    
class DataIngestion:
    
    def __init__(self):
        self.config = DataIngestionConfig()
    
    def dataset_spliter(self):
        try:
           df = pd.read_csv("Dataset/Spam_SMS.csv")
           logging.info('raw dataset Successfully saved!!')
            # label encoding
           sorce_code = {'ham':0,'spam':1}
           df['Class'] = df['Class'].map(sorce_code)
           
           # text preprocessing
           df['transform_text'] = df['Message'].apply(text_preprocessing)
           logging.info('Text preprocessing done!!')
           
           new_df = df[['transform_text','Class']]
           new_df.to_csv(self.config.processing_df)
           logging.info('Data saved Successfully!!')
           logging.info('Text preprocessing done!!')
           return self.config.processing_df
        except Exception as e:
            logging.error('Error in preprocessing data')
            raise CustomException('Error in preprocessing data')

if __name__ == '__main__':
    data_ingestion = DataIngestion()
    processing_df= data_ingestion.dataset_spliter()
    
    data_transformation = DataTransfromation()
    X_train,X_test, y_train,y_test  = data_transformation.text_vectorizer(processing_df)
    models_train = ModelTrainner()
    print('best accuracy :',models_train.train_models(X_train,X_test, y_train,y_test ))
    