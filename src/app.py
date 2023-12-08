from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel
import pandas as pd

# Load the model and encoder
model_pipeline = joblib.load('./model/xgb_pipeline.joblib')
#encoder = joblib.load('./encoder.joblib')

app = FastAPI(title="Sepsis Prediction App", version="1.0")

# Create patient features
class PatientFeatures(BaseModel):
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance: int

@app.get("/")
async def root():
    return {"message": "Welcome to the SEPSIS PREDICTION APP"}

@app.post('/PredictSepsis')
def predict_sepsis(patient_features: PatientFeatures):
    try:
        # Create a DataFrame with the input features
        input_data = pd.DataFrame([patient_features.model_dump()])


        # Make predictions using the model
        prediction = model_pipeline.predict(input_data)

        # Map prediction to 'Negative' or 'Positive'
        sepsis_status = 'Negative' if prediction[0] == 0 else 'Positive'

        return {'prediction': sepsis_status}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))