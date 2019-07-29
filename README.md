# Description
API made with Falcon to serve a machine learning model together with Celery

# Set up

### Run redis
docker run -d -p 6379:6379 redis

### Run celery
celery -A app.extensions.queue worker -l info -P eventlet/gevent

### Create conda environment
conda create -n "your_environment"
conda activate "your_environment"
pip install -r requirements.txt
python -m serve.py

### Flower


## TODO list
- Testing
- Swagger
