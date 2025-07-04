from fastapi import FastAPI
from pydantic import BaseModel
from model.predict import predict

app = FastAPI()

class Telemetry(BaseModel):
    engine_temp: float
    battery_voltage: float
    vibration_level: float
    fuel_level: float
    rpm: float
    gps_speed: float
    error_code: str

@app.post('/predict')
def predict_fault(data: Telemetry):
    result = predict(data.dict())
    return {"fault": bool(result)} 