FROM python:3

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app
 
RUN pip install elasticsearch
CMD ["python","/app/generate_dataset.py"]


