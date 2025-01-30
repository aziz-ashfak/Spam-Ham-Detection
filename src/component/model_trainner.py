import os 
import sys 
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB,ComplementNB
from sklearn.metrics import accuracy_score,confusion_matrix
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.exception import CustomException
from src.logger import logging
from src.utilts import save_data,find_the_best_model

class ModelTrainnerConfig:
    model_path = os.path.join('artifacts','model.pkl')

class ModelTrainner:
    
    def __init__(self):
        self.config = ModelTrainnerConfig()
    
    def train_models(self,X_train,X_test,y_train,y_test):
       try: 
            models = {
                    'LogisticRegression':LogisticRegression(),
                    'DecisionTreeClassifier':DecisionTreeClassifier(),
                    'ExtraTreesClassifier':ExtraTreesClassifier(),
                    'SVC':SVC(kernel='sigmoid', gamma=1.0),
                    'RandomForestClassifier':RandomForestClassifier(),
                    'KNeighborsClassifier':KNeighborsClassifier(),
                    'BaggingClassifier' :BaggingClassifier(),
                    'AdaBoostClassifier':AdaBoostClassifier(),
                    'MultinomialNB':MultinomialNB(),
                    'GradientBoostingClassifier':GradientBoostingClassifier(),
                    'GaussianNB':GaussianNB(),
                    'BernoulliNB':BernoulliNB(),
                    'ComplementNB':ComplementNB()
                    
                } 
            
            model_score = find_the_best_model(models,X_train,X_test,y_train,y_test)
            
            best_score = max(sorted(model_score.values()))
            best_model_name = list(model_score.keys())[
                list(model_score.values()).index(best_score)
                ]
            best_model = models[best_model_name]
            
            save_data(
                self.config.model_path,
                best_model
                )
            pred = best_model.predict(X_test)
            best_accuracy = accuracy_score(y_test,pred)
            logging.info('Model trained and saved Successfully!!')
            return best_accuracy
       except Exception as e:
        raise CustomException(e,sys)