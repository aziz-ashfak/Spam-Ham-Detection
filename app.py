from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import os
import sys
import nltk

nltk.download('punkt')
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from src.pipeline.predict_pipeline import make_prediction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Handle JSON request from Fetch API
        if request.is_json:
            data = request.get_json()
            message = data.get("text", "")
            if not message:
                return jsonify({"prediction": "No message provided."})
            output = make_prediction(message)
            return jsonify({"prediction": f"{output}"})
        else:
            # Handle fallback form request (optional)
            message = request.form.get('message', '')
            output = make_prediction(message)
            return render_template("home.html", prediction_text=f"{output}")

    except Exception as e:
        if request.is_json:
            return jsonify({"prediction": f"Error: {str(e)}"}), 500
        return render_template("home.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True, host='127.0.0.1', port=5000)
