import joblib
import pandas as pd
import numpy as np

def predict(input_dict):
    model = joblib.load('./model/model.pkl')
    df = pd.DataFrame([input_dict])
    # Convert error_code to numeric as in training
    df['error_code'] = df['error_code'].astype('category').cat.codes
    features = [
        'engine_temp', 'battery_voltage', 'vibration_level',
        'fuel_level', 'rpm', 'gps_speed', 'error_code'
    ]
    X = df[features]
    pred = model.predict(X)
    return int(pred[0]) 