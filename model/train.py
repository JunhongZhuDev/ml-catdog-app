import tensorflow as tf
from tensorflow.keras import layers, models

IMG_SIZE = 150
BATCH_SIZE = 32

# 读取数据（自动按文件夹分类）
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "data/",
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "data/",
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
)

# 查看类别（确认没问题）
print("Classes:", train_ds.class_names)

# 简单CNN模型
model = models.Sequential([
    layers.Rescaling(1./255),

    layers.Conv2D(16, 3, activation='relu'),
    layers.MaxPooling2D(),

    layers.Conv2D(32, 3, activation='relu'),
    layers.MaxPooling2D(),

    layers.Conv2D(64, 3, activation='relu'),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 开始训练
model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=5
)

# 保存模型
model.save("model/model.h5")

print("✅ 模型已保存到 model/model.h5")