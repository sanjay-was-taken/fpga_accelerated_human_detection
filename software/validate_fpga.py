import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load trained model
model = tf.keras.models.load_model("../output/person_detector_cnn.h5")

# Load image
img = image.load_img(
    "image.png",
    target_size=(32,32),
    color_mode='grayscale'
)

img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Software prediction
prediction = model.predict(img_array)

print("\nTensorFlow Prediction:")
print(prediction)

# FPGA output
y_fpga = 19797

# Convert back from Q8.8 scaling
z = y_fpga / 65536

print("\nRecovered FPGA Output:")
print(z)

# Sigmoid
fpga_prediction = 1 / (1 + np.exp(-z))

print("\nFPGA Prediction:")
print(fpga_prediction)