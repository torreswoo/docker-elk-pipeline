# Data generator


## local run
```
$ pip install elasticsearch
$ python generate_dataset.py
```

## docker run
```
$ docker build -t test-datagen
$ docker run --net=docker-elastic-pipeline_elk -v="${PWD}/generate_dataset.py:/app/generate_dataset.py" test-datagen
```
