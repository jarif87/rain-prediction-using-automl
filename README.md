# Rain Prediction Using AutoMl

A web application built with FastAPI and PyCaret to predict whether it will rain tomorrow based on weather-related inputs. The app features a modern, weather-inspired UI with a glassmorphism design and smooth animations.

## Features
- Predicts rain based on inputs: Humidity (3pm), Sunshine, Pressure (3pm), Cloud Cover (3pm), and Pressure (9am).
- Uses a pre-trained PyCaret classification model.
- Responsive design with a vibrant, sky-themed UI.
- Built with FastAPI, Jinja2 templates, and styled with custom CSS.

## Prerequisites
- Python 3.8+
- pip package manager

## Installation
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd rain-prediction-app
   ```
2. **Create a virtual environment:**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install dependencies:**
```
fastapi==0.115.13
Jinja2==3.1.6
numpy==1.26.4
pydantic==2.11.7
uvicorn==0.34.3
scikit-learn==1.4.2
python-multipart
pycaret==3.3.2
pandas==2.1.4
```
4. **Directory structure:**
```
rain-prediction-app/
├── static/
│   └── style.css
├── templates/
│   └── index.html
|----notebooks
├── main.py
├── rain_prediction_model.pkl
└── README.md
```
5. **Usage**
- Run the application:
```
uvicorn main:app
```

- Access the app:Open your browser and navigate to http://127.0.0.1:8000.
- Enter weather data:Input values for Humidity (3pm), Sunshine, Pressure (3pm), Cloud Cover (3pm) and Pressure (9am).
- Click "Predict Rain" to see the prediction ("Yes" or "No") and input values displayed.

## Technologies Used
- FastAPI: Web framework for building the API.
- PyCaret: Machine learning library for model loading and prediction.
- Jinja2: Templating engine for rendering HTML.
- Pandas: Data manipulation for input processing.
- CSS: Custom styling with animations and responsive design.

