import pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree

def train_model_flower():
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target
    labels = {
        0: "setosa",
        1: "versicolor",
        2: "virginica"
    }
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.5,random_state=101)

    classifier = tree.DecisionTreeClassifier()
    classifier.fit(x_train, y_train)
    pickle.dump(classifier, open('model.pkl', 'wb'))
    model = pickle.load(open('model.pkl', 'rb'))
    predictions = model.predict(x_test)
    print("Accuracy score of model :" + str(accuracy_score(y_test, predictions)))
    return model
