import numpy as np
from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

# Load the trained model from the .pkl file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the user input from the form
    ph = float(request.form['ph'])
    hardness = float(request.form['hardness'])
    solids = float(request.form['solids'])
    chloramines = float(request.form['chloramines'])
    sulfate = float(request.form['sulfate'])
    conductivity = float(request.form['conductivity'])
    organic_carbon = float(request.form['organic_carbon'])
    trihalomethanes = float(request.form['trihalomethanes'])
    turbidity = float(request.form['turbidity'])

    # Create a list of input features
    features = [[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]]

    # Make predictions using the loaded model
    prediction = model.predict(features)

    # Determine the potability label
    if prediction[0] == 1:
        result = 'Potable'
    else:
        result = 'Not Potable'

    # Render the result on the result.html template
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
