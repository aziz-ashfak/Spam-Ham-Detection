from flask import Flask,render_template,request
import pandas as pd
import numpy as  np 
import os
import sys 
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../')))
from src.pipeline.predict_pipeline import make_prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        message = request.form.get('message','')  # Preferred method

        output = make_prediction(message)
        
        return render_template('home.html',prediction_text=f"{output}")
    
    except Exception as e:
        return render_template("home.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True, host='127.0.0.1', port=5000)