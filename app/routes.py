from app.resources.APIStatus import APIStatus
from app.resources.Model import Fit, Predict
from app.resources.Task import Task, TaskStatus


def register_routes(api):
    api.add_route('/', APIStatus())
    api.add_route('/task', Task())
    api.add_route('/task/{task_id}', TaskStatus())
    api.add_route('/model/predict', Predict())
    api.add_route('/model/fit', Fit())

