import numpy as np
from app.extensions.queue import queue


class InputData:

    def __init__(self, b=-1.0, e=1.0):
        self.x = np.linspace(b, e)
        self.y = self.f(self.x)

    @staticmethod
    def f(x):
        return 3 + 0.4 * x - 3.0 * x ** 2 + 2.0 * x ** 3

    @staticmethod
    def noise(arr, fuzz):
        return arr + arr * np.random.uniform(-fuzz, fuzz, len(arr))


@queue.task(name='data.get_data')
def get_data():
    data = InputData()
    x, y = data.x, data.noise(data.y, 0.2)  # fuzz the data

    return x.tolist(), y.tolist()
