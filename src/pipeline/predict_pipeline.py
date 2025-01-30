import os 
import sys
import  pandas as pd
import  numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../')))

from src.exception import CustomException
from src.logger import logging
from src.utilts import load_data, text_preprocessing

def make_prediction(text:str):
    model_path = os.path.join('artifacts','model.pkl')
    vectorizer_path = os.path.join('artifacts','vectorizer.pkl')
    model = load_data(model_path)
    vectorizer  = load_data(vectorizer_path)
    transformed_sms = text_preprocessing(text)
    X = vectorizer.transform([transformed_sms])
    pred = model.predict(X)
    pred = np.array(pred).flatten()[0]
    if pred == 0:
        return str('This is a ham message!!!')
    else:
        return str('This is a spam message!!!')

