######curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"input": [5.1, 3.5, 1.4, 0.2]}'
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('iris_model.pkl')
@app.route('/predict',methods=['POST'])
def predict():
    data=request.get_json(force=True)
    prediction=model.predict(np.array(data['input']).reshape(1, -1))
    return jsonify({'prediction': int(prediction[0])})

if __name__== '__main__':
    app.run(host='0.0.0.0',port=5000)
# To run this Flask app, save it as serve_model.py and run it using:
# python serve_model.py
# Make sure to have Flask and joblib installed in your Python environment.
# You can send a POST request to http://localhost/predict with JSON data like:
# {
#   "input": [5.1, 3.5, 1.4, 0.2]
# }
# The response will be a JSON object with the predicted class label.
# Example response:
# {
#   "prediction": 0
# }
# Note: The model file 'iris_model.pkl' should be in the same directory as this script.
# Ensure you have Flask and joblib installed in your Python environment:
# pip install Flask joblib scikit-learn
# This code sets up a simple Flask web server that serves a machine learning model for predictions.
# The model is loaded from a file named 'iris_model.pkl', which should be created beforehand.
# The server listens for POST requests at the '/predict' endpoint, where it expects JSON data containing input features.
# The model predicts the class of the iris flower based on the input features and returns the prediction as a JSON response.
# Make sure to have the model file 'iris_model.pkl' in the same directory as this script.
# This code is a simple Flask application that serves a machine learning model for predicting iris flower species.
# The model is loaded from a file named 'iris_model.pkl', which should be created beforehand.
# The server listens for POST requests at the '/predict' endpoint, where it expects JSON data containing input features.
# The model predicts the class of the iris flower based on the input features and returns the prediction as a JSON response.
# Make sure to have the model file 'iris_model.pkl' in the same directory as this script.
# This code is a simple Flask application that serves a machine learning model for predicting iris flower species.
# The model is loaded from a file named 'iris_model.pkl', which should be created beforehand.
# The server listens for POST requests at the '/predict' endpoint, where it expects JSON data containing input features.
# The model predicts the class of the iris flower based on the input features and returns the prediction as a JSON response.
# Make sure to have the model file 'iris_model.pkl' in the same directory as this script.




