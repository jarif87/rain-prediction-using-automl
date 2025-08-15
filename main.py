from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pycaret.classification import load_model, predict_model
import pandas as pd

app = FastAPI()

# Mount the static folder for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Load the PyCaret model
model = load_model("rain_prediction_model")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "prediction": None})

@app.post("/predict")
async def predict(
    request: Request,
    humidity3pm: float = Form(...),
    sunshine: float = Form(...),
    pressure3pm: float = Form(...),
    cloud3pm: float = Form(...),
    pressure9am: float = Form(...)
):
    # Create a DataFrame from input data
    input_data = pd.DataFrame({
        "Humidity3pm": [humidity3pm],
        "Sunshine": [sunshine],
        "Pressure3pm": [pressure3pm],
        "Cloud3pm": [cloud3pm],
        "Pressure9am": [pressure9am]
    })

    # Make prediction using the loaded model
    prediction = predict_model(model, data=input_data)
    predicted_label = "Yes" if prediction["prediction_label"].iloc[0] == 1 else "No"

    # Return the template with the prediction
    return templates.TemplateResponse("index.html", {
        "request": request,
        "prediction": predicted_label,
        "input_data": input_data.to_dict(orient="records")[0]
    })