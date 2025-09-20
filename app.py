from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
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

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.is_json:
            data = request.get_json()
            message = data.get("text") or data.get("message", "")
            if not message.strip():
                return jsonify({"success": False, "error": "No message provided."}), 400

            output = make_prediction(message)
            return jsonify({"success": True, "prediction": str(output)})

        else:
            message = request.form.get('message', '')
            if not message.strip():
                return render_template("home.html", prediction_text="No message provided.")

            output = make_prediction(message)
            return render_template("home.html", prediction_text=str(output))

    except Exception as e:
        print("Prediction Error:", e, file=sys.stderr)  # log error in console
        return jsonify({"success": False, "error": str(e)}), 500
if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True, host='127.0.0.1', port=5000)
