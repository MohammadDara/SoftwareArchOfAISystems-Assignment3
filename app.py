from flask import Flask, render_template, request, jsonify
from utils import model_predict

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    title = request.form.get('title')
    prediction = model_predict(title)
    return render_template("index.html", prediction=prediction, title=title)

# Create an API endpoint
@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json(force=True)  # Get data posted as a json
    title = data['title']
    prediction = model_predict(title)
    return jsonify({'prediction': prediction, 'title': title})

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)