from pathlib import Path

import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

best_pipeline = joblib.load(MODEL_DIR / "best_model.joblib")
label_encoder = joblib.load(MODEL_DIR / "label_encoder.joblib")

def predict_pump(data: dict) -> str:
    input_df = pd.DataFrame([data])

    prediction = best_pipeline.predict(input_df)

    predicted_label = label_encoder.inverse_transform(prediction)[0]

    return predicted_label

# Load the model and perform predictons