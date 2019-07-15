import time
import numpy as np
import json
import jsonpickle
from sklearn.base import BaseEstimator, RegressorMixin


class Regressor(BaseEstimator, RegressorMixin):

    def __init__(self, degree=None, b=None, x=None, y=None, is_fitted=False):
        self.degree = degree
        self.b = b
        self.is_fitted = is_fitted
        self.x = x
        self.y = y

    def to_matrix(self, x):
        X = np.empty((len(x), self.degree + 1))
        for i in range(self.degree + 1):
            X[:, i] = np.power(x, i)

        return X

    def fit(self, x, y):
        self.x = x
        self.y = y

        x_matrix, y_matrix = self.to_matrix(x), y
        time.sleep(np.random.randint(10, 30))  # simulate slow computation
        self.b = np.linalg.pinv((x_matrix.T).dot(x_matrix)).dot((x_matrix.T).dot(y_matrix))

        self.is_fitted = True
        return self.score(self.predict(x))

    def predict(self, x):
        if self.b is None:
            raise Exception('Model not fitted!')

        x_matrix = self.to_matrix(x)
        time.sleep(np.random.randint(10, 30))  # simulate slow computation
        return x_matrix.dot(self.b)

    def score(self, y, algo='mse'):
        if algo == 'sse':
            return self._sse(y)
        elif algo == 'mse':
            return self._mse(y)
        elif algo == 'r2':
            return self._r2(y)
        else:
            raise ValueError('Evaluation algorithm not implemented')

    def _sse(self, y):
        return ((y - self.y)**2).sum()

    def _mse(self, y):
        return self._sse(y)/len(self.y)

    def _r2(self, y):
        return 1 - self._sse(y)/((self.y - self.y.mean())**2).sum()

    def get_components(self):
        return self.b.tolist()

    def save(self, path='model.json'):
        with open(path, 'w') as f:
            json.dump(jsonpickle.encode(self), f)

    def load(self, path='model.json'):

        with open(path, 'r') as f:
            m = f.read()

        loaded_model = jsonpickle.decode(json.loads(m))
        params = loaded_model.get_params()
        self.set_params(**params)
