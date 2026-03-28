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

Follow these steps to run the project locally.

---

### Step 1: Clone the repository

```bash
git clone https://github.com/<your-username>/ml-catdog-app.git
cd ml-catdog-app
```

## 2. Create a Virtual Environment

> ⚠️ This step is optional but **highly recommended** to keep your project dependencies isolated.

### 💻 Linux / macOS

```bash
# 1️⃣ Create a virtual environment named 'venv'
python -m venv venv

# 2️⃣ Activate the virtual environment
source venv/bin/activate
```

## 3. Install dependencies
pip install -r requirements.txt

This will install FastAPI, TensorFlow, Pillow, NumPy, and other required packages.

## 4. Train the model (optional if model.h5 exists)

```bash
python model/train.py
```

Run this step only if you want to train a new model. If model/model.h5 already exists, you can skip this step.

## 5. Start the FastAPI service
```bash
uvicorn api.main:app --reload
```
The server will start at http://127.0.0.1:8000.

## 6. Open the web page

Visit the following URL in your browser:

http://127.0.0.1:8000/web

Upload an image → Click Predict → The prediction result will appear on the page.

