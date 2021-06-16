from flask import Blueprint, request, jsonify
import pickle
import numpy

mlApi = Blueprint('mlApi', __name__)
model = pickle.load(open('../model.pkl', 'rb'))
labels = {
    0: "versicolor",
    1: "setosa",
    2: "virginica"
}


@mlApi.route("/predict")
def predict():
    data = request.get_json()
    print(data)
    data=numpy.array(data['feature'])
    data=data.reshape(1,-1)
    print(data)
    predictions = model.predict(data)
    print(predictions)
    return jsonify(labels[predictions[0]])
