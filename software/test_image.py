import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load model
model = tf.keras.models.load_model("../output/person_detector_cnn.h5")

# Load image
img = image.load_img(
    "test2.png",
    target_size=(32, 32),
    color_mode='grayscale'
)

# Preprocess image
img_array = image.img_to_array(img)
img_array = img_array / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Predict
prediction = model.predict(img_array)

confidence = prediction[0][0]

print("\nRaw Output:", confidence)

if confidence > 0.5:
    print(f"PERSON detected ({confidence*100:.2f}% confidence)")
else:
    print(f"NO PERSON ({(1-confidence)*100:.2f}% confidence)")