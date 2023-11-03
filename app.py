# simple endpoint app
from flask import Flask, request, jsonify
from joblib import load
import pandas as pd

app = Flask(__name__)

def load_model(f = 'model.joblib'):
    model = load(f)
    return model

@app.route('/')
def home():
    """
        this is the home page
    """
    return "Hello World!"

@app.route('/predict', methods = ['POST'])
def predict():
    data = pd.DataFrame.from_dict(request.get_json())
    model = load_model()
    pred = model.predict(data)
    return jsonify({'predictions':list(pred)})


# Start the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
