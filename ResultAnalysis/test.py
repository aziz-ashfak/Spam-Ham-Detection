import os 
import sys
import  pandas as pd
import  numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../')))
from src.exception import CustomException
from src.logger import logging
from src.pipeline.predict_pipeline import make_prediction

make_prediction("Hi ,how are you?")