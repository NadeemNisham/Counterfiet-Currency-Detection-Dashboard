from keras.models import load_model
import tensorflow as tf
import tensorflow.keras.preprocessing.image as preprocess
import pandas as pd
import numpy as np

print(">> Loading model >>")
# Load the saved models
model = load_model("models/latest_inceptionv3.h5")


def predict_value(model, image):
    # Create a Pandas DataFrame containing the path of the image to predict
    data = pd.DataFrame(list(image.getdata()))

    predict_datagen = preprocess.ImageDataGenerator(rescale=1. / 255)
    predict_generator = predict_datagen.flow_from_dataframe(
        data,
        x_col='filename',
        y_col=None,
        class_mode=None,
        target_size=(512, 512),
        batch_size=1,
        shuffle=False,
        preprocessing_function=lambda x: x / 255.0 - 0.5
    )

    # Make predictions on the image to predict
    predictions = model.predict(predict_generator, steps=len(predict_generator), verbose=1)

    # Convert the predictions to class labels
    predicted_class_index = np.argmax(predictions)

    classes = ["100", "1000", "20", "50", "500", "5000"]
    value = classes[predicted_class_index]

    return value


value = 0


def main(image):
    global value
    value = predict_value(model, image)


def get_value():
    return value
