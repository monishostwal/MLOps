from flask import Blueprint, request, jsonify,Flask
import pickle
import numpy


app=Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
labels = {
    0: "versicolor",
    1: "setosa",
    2: "virginica"
}

@app.route('/')
def ok():
	return "OK"

@app.route('/flowers/predict')
def check():
	data = request.get_json()
	print(data)
	data=numpy.array(data['feature'])
	data=data.reshape(1,-1)
	print(data)
	predictions = model.predict(data)
	print(predictions)
	return jsonify(labels[predictions[0]])


if __name__=='__main__':
    app.run(debug=True)
