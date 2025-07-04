import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv('../data/telemetry.csv')

features = [
    'engine_temp', 'battery_voltage', 'vibration_level',
    'fuel_level', 'rpm', 'gps_speed', 'error_code'
]

# Convert categorical error_code to numeric
df['error_code'] = df['error_code'].astype('category').cat.codes

X = df[features]
y = df['label']

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

# Save model
joblib.dump(clf, 'model.pkl') 