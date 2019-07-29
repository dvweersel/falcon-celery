import os
import numpy as np
import json
import jsonpickle
from sklearn.base import BaseEstimator, RegressorMixin


class Regressor(BaseEstimator, RegressorMixin):

    def __init__(self, degree=None, b=None, is_fitted=False, mse=None):
        self.degree = degree
        self.b = b
        self.is_fitted = is_fitted
        self.mse = mse

    def to_matrix(self, x):
        X = np.empty((len(x), self.degree + 1))
        for i in range(self.degree + 1):
            X[:, i] = np.power(x, i)

        return X

    def fit(self, x, y):
        X, y_matrix = self.to_matrix(x), y
        self.b = np.linalg.pinv(X.T.dot(X)).dot(X.T.dot(y_matrix))

        self.is_fitted = True
        self.mse = self.score(x, y)

    def predict(self, x):
        if self.b is None:
            raise Exception('Model not fitted!')

        X = self.to_matrix(x)
        return X.dot(self.b)

    def score(self, X, y):
        pred = self.predict(X)
        return ((pred - y)**2).sum()

    def get_components(self):
        return self.b.tolist()

    def save(self, path='app/model/model.json'):
        with open(path, 'w') as f:
            json.dump(jsonpickle.encode(self), f)

    def load(self, path='app/model/model.json'):

        if os.path.exists(path):
            with open(path, 'r') as f:
                m = f.read()

            loaded_model = jsonpickle.decode(json.loads(m))
            params = loaded_model.get_params()
            self.set_params(**params)
        else:
            raise FileNotFoundError(f"No model found at {path}")
