from flask import Flask, request
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    result = model.predict([[data['protein'], data['fat'], data['carbs']]])
    return {"calories": float(result[0])}

app.run(host='0.0.0.0', port=5000)
