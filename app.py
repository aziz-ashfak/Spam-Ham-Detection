from flask import Flask, render_template, request, jsonify
import os
import sys
import nltk

# Download punkt only if not already available
nltk.download('punkt', quiet=True)

# Add src path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
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
            message = data.get("text", "")
            if not message:
                return jsonify({"prediction": "No message provided."})
            output = make_prediction(message)
            return jsonify({"prediction": str(output)})
        else:
            message = request.form.get('message', '')
            output = make_prediction(message)
            return render_template("home.html", prediction_text=str(output))
    except Exception as e:
        if request.is_json:
            return jsonify({"prediction": f"Error: {str(e)}"}), 500
        return render_template("home.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gives you PORT
    app.run(debug=False, host="0.0.0.0", port=port)

