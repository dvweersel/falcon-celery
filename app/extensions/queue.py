import os
from celery import Celery


queue = Celery('queue', broker=os.environ['CELERY_BROKER'], backend=os.environ['CELERY_BACKEND'])
