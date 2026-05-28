import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
import numpy as np
import os

os.makedirs("../output", exist_ok=True)

# Dataset paths
train_dir = "dataset/train"
val_dir = "dataset/val"

# Parameters
IMG_SIZE = (32, 32)
BATCH_SIZE = 32
EPOCHS = 20

# Data generators
train_datagen = ImageDataGenerator(rescale=1.0/255.0)
val_datagen = ImageDataGenerator(rescale=1.0/255.0)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=IMG_SIZE,
    color_mode='grayscale',
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=IMG_SIZE,
    color_mode='grayscale',
    batch_size=BATCH_SIZE,
    class_mode='binary'
)

# Lightweight CNN
model = Sequential([
    Conv2D(8, (3,3), activation='relu', input_shape=(32,32,1)),
    MaxPooling2D(2,2),

    Conv2D(16, (3,3), activation='relu'),
    MaxPooling2D(2,2),

    Flatten(),

    Dense(16, activation='relu'),

    Dense(1, activation='sigmoid')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print("\nModel Summary:")
model.summary()

# Train
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=EPOCHS
)

# Accuracy
print("\nFinal Training Accuracy:",
      history.history['accuracy'][-1])

print("Final Validation Accuracy:",
      history.history['val_accuracy'][-1])

# Save model
model.save("../output/person_detector_cnn.h5")

print("\nModel saved successfully")

# Extract dense layer weights
dense1_weights, dense1_biases = model.layers[-2].get_weights()
dense2_weights, dense2_biases = model.layers[-1].get_weights()

# Save weights
np.save("../output/dense1_weights.npy", dense1_weights)
np.save("../output/dense1_biases.npy", dense1_biases)

np.save("../output/dense2_weights.npy", dense2_weights)
np.save("../output/dense2_biases.npy", dense2_biases)

print("\nDense layer weights exported")