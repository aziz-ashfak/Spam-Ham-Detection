from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import os
import sys 
import  pandas as pd
import numpy as np
from imblearn.combine import  SMOTETomek
from sklearn.model_selection import train_test_split
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.exception import CustomException
from src.logger import logging
from src.utilts import save_data,text_preprocessing
class DataTransformationConfig:
    vectorizer = os.path.join('artifacts','vectorizer.pkl')
class DataTransfromation:
    def __init__(self):
        self.config = DataTransformationConfig()
    def text_vectorizer(self,procsessing_path):
        try:
            df = pd.read_csv(procsessing_path)
            # train_df = pd.read_csv(train_path)
            # test_df = pd.read_csv(test_path)
            logging.info('Data loaded Successfully!!')
            
            df['transform_text'] = df['transform_text'].astype(str)
            Tfidf = TfidfVectorizer(stop_words='english')

            X = Tfidf.fit_transform(df['transform_text']).toarray()
            y = df['Class'].values
            # imbalance data handling
            sm = SMOTETomek()
            resample_X,resample_y = sm.fit_resample(X,y)
            # vectorization
            # Tfidf = TfidfVectorizer()
            # X_train = Tfidf.fit_transform(train_df['transform_text']).toarray()
            # X_test = Tfidf.transform(test_df['transform_text']).toarray()
            # logging.info('Data vectorization done!!')
            # # label encoding
            # y_train = train_df['Class']
            # y_test = test_df['Class']
            X_train,X_test, y_train,y_test = train_test_split(resample_X,resample_y,test_size=0.2,random_state=42)
            save_data(
                path=self.config.vectorizer,
                obj=Tfidf
                )
            logging.info('Vectorizer saved Successfully!!')
            return X_train,X_test, y_train,y_test 
        except Exception as e:
           raise CustomException(e,sys)