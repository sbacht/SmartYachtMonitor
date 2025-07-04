# Smart Yacht Monitor

## 🌊 Description
"Smart Yacht Monitor" is a pet project that demonstrates the full MLOps cycle for monitoring the condition of a yacht based on IoT data. The system analyzes telemetry from sensors (engine temperature, voltage, vibration, etc.) and predicts potential technical problems, enabling proactive maintenance.

The project includes:
- Telemetry data generation
- Fault prediction model training
- REST API for model inference (FastAPI)
- Data logging to PostgreSQL
- Monitoring (Evidently / Grafana)
- Retraining pipeline (Airflow + MLflow)

## 📊 Project Structure
```
smart-yacht-monitor/
├── data/                      # Generator and sample data
│   └── telemetry.csv         
├── notebooks/                # Analysis and model training
│   └── eda_and_model.ipynb
├── model/
│   ├── train.py              # Model training script
│   ├── predict.py            # Model inference
│   └── model.pkl             # Saved model
├── api/
│   └── main.py               # FastAPI server
├── airflow/
│   └── dag.py                # DAG for retraining
├── mlflow/                   # Experiment logs
├── docker/
│   ├── Dockerfile.api        # API container
│   └── Dockerfile.train      # Training container
├── docker-compose.yml        # Full system setup
├── requirements.txt          # Dependencies
└── README.md                 # Project description
```

## 🚀 How to Run (Locally)
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Train the model:
```bash
python3 model/train.py
```

3. Start the API:
```bash
uvicorn api.main:app --reload
```

4. Send telemetry JSON:
```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"engine_temp": 92, "battery_voltage": 11.8, "vibration_level": 0.6, "fuel_level": 55, "rpm": 3200, "gps_speed": 6.1, "error_code": "None"}'
```

## 🎓 Project Goals
- Learn the full MLOps pipeline from data to production
- Practice with FastAPI, Docker, MLflow, Airflow
- Create a useful project for portfolio or startup

---

📉 Author: Serge Bacht
🚀 Free to use and modify
