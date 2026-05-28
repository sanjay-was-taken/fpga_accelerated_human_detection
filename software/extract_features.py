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

# Extract Dense(16) features
intermediate_model = tf.keras.Model(
    inputs=model.inputs,
    outputs=model.layers[-2].output
)

features = intermediate_model.predict(img_array)

print("\nExtracted Features:")
print(features)

# Convert to fixed-point
scale = 256

fixed_inputs = (features * scale).round().astype(int)

print("\nFixed-point FPGA Inputs:")
print(fixed_inputs)

# Final prediction
prediction = model.predict(img_array)

print("\nTensorFlow Prediction:")
print(prediction)