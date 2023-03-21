from flask import Flask, render_template

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
        return render_template('identify_currency.html', prediction=prediction)
    else:
        return render_template('identify_currency.html')
    
@app.route('/sum_up_currency', methods=['GET', 'POST'])
def sum_up_currency():
    if request.method == 'POST':
        files = request.files.getlist('images')
        sum = 0
        for file in files:
            image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
            prediction = identify(image)
            sum = sum + int(prediction)
        return render_template('sum_up_currency.html', prediction=sum)
    else:
        return render_template('sum_up_currency.html')

if __name__ == '__main__':
    app.run(debug=True)
