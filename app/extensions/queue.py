from dotenv import load_dotenv
load_dotenv()
import os
from celery import Celery


queue = Celery('queue', broker=os.environ['CELERY_BROKER'], backend=os.environ['CELERY_BACKEND'])

if __name__ == '__main__':
    queue.start()