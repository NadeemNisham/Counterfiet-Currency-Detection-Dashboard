import tensorflow as tf
from tensorflow import keras
import cv2
import numpy as np
import identify_note as note

def predict_value(model, image):
    # Preprocess the image
    image = cv2.resize(image, (512, 512))
    image_array = image / 255.0 - 0.5
    image_array = np.expand_dims(image_array, axis=0)

    # Make predictions on the image
    predictions = model.predict(image_array, verbose=1)

    # Convert the predictions to class labels
    predicted_class_index = np.argmax(predictions)

    classes = ["100", "1000", "20", "50", "500", "5000"]
    value = classes[predicted_class_index]

    return value
