import json
import time
import numpy as np
import celery
from app.extensions.queue import queue


class Task:

    @staticmethod
    def on_get(req, resp):
        """
            Create a task and returns ID
        """
        task = make_task.delay()
        resp.body = json.dumps(f'Created task with ID {task.id}')


class TaskStatus:
    @staticmethod
    def on_get(req, resp, task_id):
        try:
            task = celery.result.AsyncResult(task_id, queue.backend)
            if task.status == 'SUCCESS':
                resp.body = json.dumps({'task': task.result})
            else:
                resp.body = json.dumps("Task {} status is '{}'".format(task_id, task.status))
        except AttributeError:
            resp.body = json.dumps("Unknown task ID: '{}'".format(task_id))


@queue.task
def make_task():
    time.sleep(np.random.randint(10, 20))  # simulate slow computation
    return "Task completed"