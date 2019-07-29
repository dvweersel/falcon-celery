FROM python:3.7-slim

# set /app as working directory
ENV APP_DIR /app
WORKDIR ${APP_DIR}

# copy the codebase
ADD ./ ${APP_DIR}/

# install requirements
RUN pip install -r requirements.txt