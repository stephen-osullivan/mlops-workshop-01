from app import load_model
import pandas as pd
import numpy as np

def test_load_model():
    try:
        model = load_model()
        assert True
    except:
        assert False

def test_predict_model():
    try:
        model = load_model()
        df = pd.read_json('sample_predictions.json')
        preds = model.predict(df)
        assert len(preds) == 3
        assert all(np.in1d(preds, ['malignant', 'benign']))
    except:
        assert False