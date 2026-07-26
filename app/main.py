from fastapi import FastAPI

from app.routes import router

app = FastAPI(
    title="Tanzania Water Pump Prediction API",
    description="Predicts the operational status of a water pump"
)

app.include_router(router)



#Create and config the FastAPI app