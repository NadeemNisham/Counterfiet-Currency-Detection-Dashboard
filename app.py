from flask import Flask, render_template, request
import numpy as np
import cv2
from predict import identify, classify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/identify_currency', methods=['GET', 'POST'])
def identify_currency():
    if request.method == 'POST':
        file = request.files['image']
        image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
        prediction = identify(image)
        return render_template('identify.html', prediction=prediction)
    else:
        return render_template('identify.html')


@app.route('/sum_up_currency', methods=['GET', 'POST'])
def sum_up_currency():
    if request.method == 'POST':
        files = request.files.getlist('images')
        sum = 0
        for file in files:
            image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
            prediction = identify(image)
            sum = sum + int(prediction)
        return render_template('sumup.html', prediction=sum)
    else:
        return render_template('sumup.html')


@app.route('/classify_note', methods=['GET', 'POST'])
def classify_note():
    if request.method == 'POST':
        file = request.files['image']
        uv_file = request.files['uv-image']
        image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
        uv_image = cv2.imdecode(np.fromstring(uv_file.read(), np.uint8), cv2.IMREAD_COLOR)
        prediction = classify(image, uv_image)
        return render_template('classify.html', prediction=prediction)
    else:
        return render_template('classify.html')

@app.route('/about_us')
def about_us():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
