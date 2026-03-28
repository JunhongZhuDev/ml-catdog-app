from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from PIL import Image
import numpy as np
import tensorflow as tf
import os

app = FastAPI()

# 允许所有来源（开发阶段）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 加载模型（启动时执行一次）
model = tf.keras.models.load_model("model/model.h5")

def preprocess(image):
    image = image.resize((150, 150))
    image = np.array(image) / 255.0
    return np.expand_dims(image, axis=0)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    img = preprocess(image)
    pred = model.predict(img)[0][0]
    label = "Dog" if pred > 0.5 else "Cat"
    return {
        "prediction": label,
        "confidence": float(pred)
    }

# =========================
# 前端网页整合
# =========================

# 挂载 frontend 目录为 /static
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/web")
def serve_frontend():
    # 返回网页 index.html
    return FileResponse("frontend/index.html")