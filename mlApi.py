from flask import Blueprint, request, jsonify, Flask
import pickle
import numpy
import train_model

app = Flask(__name__)
labels = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}


@app.route('/flowers/predict')
def check():
    model = train_model.train_model_flower()
    data = request.get_json()
    print("Data received : "+str(data))
    data = numpy.array(data['feature'])
    data = data.reshape(1, -1)
    predictions = model.predict(data)
    print(predictions)
    return jsonify(labels[predictions[0]])


if __name__ == '__main__':
    app.run(debug=True)
