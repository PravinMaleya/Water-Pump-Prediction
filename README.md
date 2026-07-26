## Tanzania Water Pump Status Prediction API

A machine learning-powered REST API built with **FastAPI** that predicts the operational status of water pumps in Tanzania. The API serves predictions from a trained machine learning model through a simple REST interface, demonstrating an end-to-end machine learning deployment workflow.

---

### Business Problem

Access to clean and reliable water is essential for improving public health and supporting economic development. Across Tanzania, thousands of water pumps have been installed to provide communities with safe drinking water. However, many pumps eventually become non-functional due to mechanical failures, poor maintenance, environmental conditions, or resource constraints.

Organizations responsible for maintaining these water points often face limited budgets and personnel, making it difficult to inspect every pump regularly. An intelligent system capable of predicting a pump's operational status can help prioritize maintenance efforts, improve resource allocation, and reduce downtime for affected communities.

This project addresses that challenge by using machine learning to classify the operational status of water pumps based on their physical characteristics, location, management, and other operational features.

---

## Project Objectives

The objectives of this project are to:

* Build a machine learning model capable of predicting the operational status of water pumps.
* Deploy the trained model as a REST API using FastAPI.
* Validate incoming requests using Pydantic models.
* Return real-time predictions through HTTP endpoints.
* Demonstrate best practices for structuring and deploying a machine learning application.

---

## Dataset

The model was trained using historical water pump data containing demographic, geographical, operational, and management-related information.

Examples of features include:

* Amount of water available (`amount_tsh`)
* GPS elevation (`gps_height`)
* Population served
* Pump age
* Water source
* Basin
* Region
* Water quality
* Payment type
* Management group
* Extraction type
* Permit status

The target variable is the operational status of each water pump.

---

## Methodology

The project follows a typical machine learning deployment pipeline:

1. Collect and preprocess the dataset.
2. Engineer relevant features.
3. Train and evaluate multiple machine learning models.
4. Save the best-performing model using Joblib.
5. Deploy the trained model using FastAPI.
6. Expose prediction endpoints through a REST API.

---

## Project Structure

```text
water_pump_prediction/
│
├── app/
│   ├── main.py          # Application entry point
│   ├── routes.py        # API endpoints
│   ├── predictor.py     # Prediction logic
│   ├── schemas.py       # Pydantic models
│
├── data/
│   ├── raw/
│   │   ├── features.csv
│   │   └── labels.csv
│   └── processed/
│       └── cleaned.csv
│
├── models/
│   ├── best_model.joblib
│   └── label_encoder.joblib
│
├── notebooks/
├── requirements.txt
├── .gitignore
└── README.md

---

Technologies Used

* Python
* FastAPI
* Pandas
* Scikit-learn
* Joblib
* Pydantic
* Uvicorn
* Jupyter Notebook

---

Installation

Clone the repository:

```bash
git clone <https://github.com/PravinMaleya/Water-Pump-Prediction>
```

Navigate into the project directory:

```bash
cd water_pump_prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running the API

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### Home Endpoint

**GET /**

Returns a confirmation message indicating that the API is running.

Example response:

```json
{
    "message": "Water Prediction API is running"
}
```

---

### Prediction Endpoint

**POST /predict**

Accepts water pump characteristics and returns the predicted operational status.

Example response:

```json
{
    "prediction": "functional"
}
```

---

## Results

The deployed API successfully serves predictions from the trained machine learning pipeline by:

* Validating incoming requests.
* Transforming input data into the required format.
* Loading the trained model.
* Predicting the operational status.
* Returning predictions as JSON responses.

---

## Future Improvements

Future enhancements for this project include:

* Docker containerization
* Cloud deployment (Azure, AWS, Render, Railway)
* Automated model retraining
* CI/CD with GitHub Actions
* Unit and integration testing
* Model monitoring and logging
* Prediction confidence scores
* Authentication and rate limiting

---

## Author

**Pravin Maleya**

