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


def identify(image):
    model = keras.models.load_model(
        "D:\College Material\Lectures\Year 2\Semester 2\CM2603 - Data Science Group Project\Project\dashboard test\models\identify.h5")
    return predict_value(model, image)


def classify(image, uv_image):
    value = identify(image)
    # change value later
    value = '20'
    classification = classify_image(uv_image, value)
    return classification


def classify_image(uv_image, value):
    rgb = cv2.cvtColor(uv_image, cv2.COLOR_BGR2RGB)
    resized = tf.image.resize(rgb, (120, 120))
    model = keras.models.load_model('models/fake-' + value + '.h5')
    yhat = model.predict(np.expand_dims(resized / 255, 0))
    if yhat[0] > 0.99:
        return 'Real'
    else:
        return 'Fake'
