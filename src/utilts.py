import pickle 
import sys
import os
import nltk
import pandas as pd
import numpy as np
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string
from sklearn.metrics import accuracy_score,confusion_matrix
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))   
from src.exception import CustomException
from src.logger import logging
def save_data(path,obj):
    try:
        with open(path,"wb") as file_obj:
            pickle.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)

def load_data(path):
    try:
        with open(path,"rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def text_preprocessing(text):
        ps  = PorterStemmer()
        text = text.lower()
        text = nltk.word_tokenize(text)
        y =[]

        for i in text:
            if i.isalnum(): # remove special chacrecters
                y.append(i)
        text = y[:]
        y.clear()

        for i in text:
            if i not in stopwords.words('english') and i not in string.punctuation:
                y.append(i)
        text = y[:]
        y.clear()
        for i in text:
            y.append(ps.stem(i))
        return " ".join(y)
    
def find_the_best_model(models,X_train,X_test, y_train,y_test):
    accuracy = []
    matrix = []
    report = {}
    for i in range(len(models)):
        model = list(models.values())[i]
        model_name = list(models.keys())[i]
        model.fit(X_train,y_train)
        pred = model.predict(X_test)
        acc = accuracy_score(y_test,pred)
        print(f"{model_name}: \n accuracy :",acc)
        accuracy.append(acc)
        confo_mat = confusion_matrix(y_test,pred)
        print(" cofusion_matrix :\n",confo_mat)
        matrix.append(confo_mat)
        report[model_name] = acc
    result = {
        'Model':list(models.keys()),
        'Accuracy':accuracy
    }
    result = pd.DataFrame(result)
    result.to_csv('ResultAnalysis/result.csv')
    np.save('ResultAnalysis/confusion_matrix.npy',matrix)
    return report