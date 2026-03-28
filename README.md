# 🐱🐶 Cat vs Dog Classifier

## Project Overview

This is an **end-to-end machine learning project** that allows you to upload an image via a web page and predict whether it is a cat or a dog.  
The project includes **model training, API backend, and frontend web interface**, and can also be deployed to cloud platforms (e.g., Render) for public access.

---

## Project Structure

ml-catdog-app/
│
├── data/                # Dataset
├── model/
│   ├── train.py         # Train the model
│   └── model.h5         # Save the model
│
├── api/
│   └── main.py          # FastAPI interface
│
├── frontend/
│   └── index.html       # Frontend
│
├── requirements.txt
├── README.md
└── .gitignore


---

## Features

- **Image Upload & Prediction**: Supports JPG/PNG images; click "Predict" to see the result.  
- **Model Prediction**: Uses a TensorFlow/Keras convolutional neural network model.  
- **Frontend-Backend Integration**: FastAPI provides the `/predict` endpoint; the frontend calls it via AJAX.  
- **Local & Cloud Deployment**: Can run locally or be deployed to cloud platforms like Render.  

---

## Quick Start (Local)

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ml-catdog-app.git
cd ml-catdog-app

# Linux/macOS
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

uvicorn api.main:app --reload

http://127.0.0.1:8000/web