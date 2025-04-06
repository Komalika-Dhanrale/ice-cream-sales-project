from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model/linear_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp = float(request.form['temperature'])
    prediction = model.predict(np.array([[temp]]))[0]
    return render_template('result.html', temperature=temp, profit=round(prediction, 2))

if __name__ == '__main__':
    app.run(debug=True)
