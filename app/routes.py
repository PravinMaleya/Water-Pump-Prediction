from fastapi import APIRouter

from app.schemas import PumpData
from app.predictor import predict_pump

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "Water Prediction API is running"
    }


@router.post("/predict")
def predict(data: PumpData):
    prediction = predict_pump(data.model_dump())

    return {
        "Predicted Status Group": prediction
    }




#Defines endpoints and handles requests