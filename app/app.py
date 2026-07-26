# from fastapi import FastAPI
# from pydantic import BaseModel
# import pandas as pd
# import joblib

# # Load saved models and encoded labels
# #best_pipeline = joblib.load('C:\Users\dell\Desktop\Projects\water_pump_prediction\models\best_model.joblib')
# #label_encoder = joblib.load('C:\Users\dell\Desktop\Projects\water_pump_prediction\models\label_encoder.joblib')

# from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# MODEL_DIR = BASE_DIR / "models"

# best_pipeline = joblib.load(MODEL_DIR / "best_model.joblib")
# label_encoder = joblib.load(MODEL_DIR / "label_encoder.joblib")

# # Create FastaAPI app
# app = FastAPI(
#     title = 'Tanzania Water Prediction API',
#     description = 'Predicts the operational status of a waterpump'
# )

# # Blueprint for variable dtypes - pydantic
# # input schema
# class PumpData(BaseModel):
#      amount_tsh: float
#      gps_height: int
#      population: int
#      age: float
#      month_recorded: int
#      permit: bool   
#      waterpoint_type_group: str    
#      source_class: str    
#      quantity: str    
#      quality_group: str    
#      payment_type: str    
#      management_group: str    
#      extraction_type_class: str    
#      region: str    
#      basin: str    

# @app.get('/')
# def home():
#      return {'message': 'Water Prediction API is running'}


# #prediction endpoint
# @app.post('/predict')
# def predict(data: PumpData):
#      input_df = pd.DataFrame([data.model_dump()])

#      prediction = best_pipeline.predict(input_df)
#      predicted_label = label_encoder.inverse_transform(prediction)[0]
#      return{'Predicted Status group': predicted_label}

